from flask import Flask,session
import threading 
import time
import requests
import json
from datetime import datetime
from flask_cors import CORS
from rtu_app.utility import get_value_syn,set_value,get_centigrade,open_read_virtual,save_virtual,open_write_virtual,get_compresors
from rtu_app.main import init_vars
from rtu_app.schedule import init_schedule_vars
from rtu_app.alarm import init_alarm_vars
from rtu_app.alarm_limits import init_alarmlim_vars
from rtu_app.gen_settings import init_general_vars
from rtu_app.sensor_limit import init_sensorlim_vars
from rtu_app.sensor_fail import init_fail_vars
from rtu_app.setpoint import init_setpoint_vars
from rtu_app.energy import init_energy_vars
from rtu_app.main import init_vars
from rtu_app.speed_limit import init_speedlim_vars
from rtu_app.air_sensor import init_sensors,read_sensors,get_sensors,write_sensors
from rtu_app.read_values import init_read_vars,update_read_vars
from rtu_app.write_values import init_write_vars,update_write_vars
app = Flask(__name__)
#app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.secret_key = "mysecretkey"
CORS(app)

version=4.00

global rtu_main_vars
global rtu_energy_vars
global rtu_alarm_vars
global rtu_fail_vars
global rtu_setpoint_vars
global rtu_alarmlim_vars
global rtu_sensorlim_vars
global rtu_schedule_vars
global rtu_miscell_vars
global rtu_speedlim_vars
#global historic_vars

rtu_main_vars=[]
rtu_energy_vars=[]
rtu_alarm_vars=[]
rtu_fail_vars=[]
rtu_setpoint_vars=[]
rtu_alarmlim_vars=[]
rtu_sensorlim_vars=[]
rtu_schedule_vars=[]
rtu_miscell_vars=[]
rtu_speedlim_vars=[]
historic_vars=[]
air_buffer=[]
config_sensor ={}
sensor_values={}
air_sampling=False
rtu_read_vars=[]
rtu_write_vars=[]
buffer_web=[]
dynamic_web=[18,1,2]
error_web=[0,0,0,0,0]
dynamic_air=[0]

def update_buffer(buffer_list):
   global config_sensor
   buffindex = [46,6,42,43,44,45,145,168]
   if len(buffer_list)>=120: #1440:
     buffer_list.pop(0)
#     buffer_list=buffer_list[-1439:0]
   var = []     
   for i in range(len(buffindex)):
      rsp=get_value_syn(buffindex[i])
      if rsp is not None:
        if i==1 or i==7:
          if config_sensor['conv']>0:
               rsp=get_centigrade(rsp)
        
        var.append(rsp)
      else:
        var.append(0)  
      
   #tt=int(time.time())   
   now = datetime.now()   
#   dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   dt_string = now.strftime("%H:%M")
   var.append(dt_string)
   buffer_list.append(var)


   
def save_hist_buffer():
    global historic_vars
    while True:
      time.sleep(58)
      update_buffer(historic_vars)

def save_air_buffer():
    global air_buffer
    global config_sensor
    today = datetime.now()
    day=today.day
    config_sensor['buffer_air_month']=today.month
    config_sensor['buffer_air_year']=today.year
    if day!=config_sensor['buffer_air_day']:
      config_sensor['buffer_air_day']=day
      write_sensors(config_sensor)
      air_buffer.clear()
    if len(air_buffer)<145:
      var = []
      var.append(today.hour)
      var.append(today.minute)
      var.append(today.second)
      var.append("{:.0f}".format(sensor_values['score']))
      var.append("{:.0f}".format(sensor_values['temp']))
      var.append("{:.0f}".format(sensor_values['humid']))
      var.append("{:.0f}".format(sensor_values['co2']))
      var.append("{:.0f}".format(sensor_values['voc']))
      var.append("{:.0f}".format(sensor_values['pm25']))
      var.append(config_sensor['mac_iaq'])
      air_buffer.append(var)
      config_sensor['buffer_air_avail']=1

        

def web_task():
    global config_sensor
    global rtu_read_vars
    global dynamic_web
    global event_web
    global buffer_web
    global version
    global error_web
    while config_sensor['web_period']>0:
      if config_sensor['user_rtu']>0:
          if config_sensor['trend_opc']!=1:
            web_check()
            if config_sensor['send_command']>0:
              web_command()
          dynamic_web[0]=dynamic_web[0]-dynamic_web[1]
          if dynamic_web[0]<=0 or config_sensor['force_upload']>0: 
            dynamic_web[0]=6*config_sensor['web_period']
            config_sensor['force_upload']=0
            now = datetime.now()   
            dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
            config_sensor['last_upload']=dt_string
            if config_sensor['trend_opc']!=1:
              update_read_vars(rtu_read_vars)
              buffer_web.clear()
              buffer_web.append(35) #envio desde el controlador
              buffer_web.append(config_sensor['user_rtu'])
              buffer_web.append(dt_string)
              buffer_web.append(version)
              buffer_web.append(config_sensor['total_rtus']) 
              buffer_web.append(config_sensor['rtu_number']) 
              buffer_web.append(len(rtu_read_vars))
              for i in range(len(rtu_read_vars)):
                buffer_web.append(rtu_read_vars[i]['addr'])
                buffer_web.append(rtu_read_vars[i]['name'])
                buffer_web.append(rtu_read_vars[i]['value'])
                buffer_web.append(rtu_read_vars[i]['Ident'])
                buffer_web.append(rtu_read_vars[i]['Type'])
                buffer_web.append(rtu_read_vars[i]['Unit'])
                buffer_web.append(0) #error
              buffer_web.append(config_sensor['conv'])  
              try:
                url='http://www.greenmediahd.com/rooftop/api_rtu_sc.php'
                rsp = requests.post(url, data=json.dumps(buffer_web) , timeout=4)
                error_web[0]=rsp.status_code
              except:
                error_web[0]=533
              if config_sensor['user_aqs']>0:
                  web_iaq()
              if config_sensor['trend_opc']>1:
                  web_trending()
              if error_web[2]==555:
                  web_command() #repeat command if error
            else: #only trending required
              web_trending()        
      event_web.wait(10)           
      #time.sleep(58)
    event_web.clear()
    
    

def web_check():
          global config_sensor
          global version
          url='http://www.greenmediahd.com/rooftop/api_rtu_comm_check.php?ucode='+str(config_sensor['user_rtu'])+'&rtu='+str(config_sensor['rtu_number'])
          me=[]
          try:
            rsp = requests.get(url, timeout=2)
            if (rsp.status_code == 200):
              values=rsp.json()
              if values[0]>0:
                load_command()
              elif values[1]>0:
                config_sensor['force_upload']=1
              return values
          except:
            return me
            #me=1

def load_command():
          global config_sensor
          global version
          url='http://www.greenmediahd.com/rooftop/api_commander_rtu.php?ucode='+str(config_sensor['user_rtu'])+'&rtu='+str(config_sensor['rtu_number'])
          me=0
          try:
            rsp = requests.get(url, timeout=2)
            if (rsp.status_code == 200):
              values=rsp.json()
              cant=int(values[0])
              cad='';
              index=1
              for i in range(cant):
                instance = int(values[index]);
                objtype = int(values[index + 1]);
                value = float(values[index + 2]);
                index += 3;
                for i in range(len(rtu_write_vars)):
                  if rtu_write_vars[i]['Ident']==instance and rtu_write_vars[i]['Type']==objtype:
                    ii=rtu_write_vars[i]['index'];
                    if set_value(ii,value)<0: 
                      #cad=cad+f'Error Intance: {instance} Type: {objtype} Value: {value} Index {ii}'
                      #cad=cad+f' Value: {value} set successfully'                   
                      me=1
                    config_sensor['send_command']=1  
               # cad=cad+f' Intance: {instance} Type: {objtype} Value: {value} '
              #return cad  
            else:
              me=1
          except:
            me=1
                
def web_command():
          global config_sensor
          global rtu_write_vars
          global buffer_web
          global error_web
          config_sensor['send_command']=0
          update_write_vars(rtu_write_vars)
          buffer_web.clear()
          buffer_web.append(35) #envio desde el controlador
          buffer_web.append(config_sensor['user_rtu'])
          now = datetime.now()   
          dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
          buffer_web.append(dt_string)
          buffer_web.append(config_sensor['rtu_number']) 
          buffer_web.append(len(rtu_write_vars))
          for i in range(len(rtu_write_vars)):
            buffer_web.append(rtu_write_vars[i]['addr'])
            buffer_web.append(rtu_write_vars[i]['name'])
            buffer_web.append(rtu_write_vars[i]['value'])
            buffer_web.append(rtu_write_vars[i]['Ident'])
            buffer_web.append(rtu_write_vars[i]['Type'])
            buffer_web.append(rtu_write_vars[i]['Unit'])
            buffer_web.append(0) #error
          url='http://www.greenmediahd.com/rooftop/api_rtu_comm.php'
          try:
            rsp = requests.post(url, data=json.dumps(buffer_web) , timeout=4)
            #error_web.append(rsp.text)
            if rsp.status_code!=200:
              error_web[2]=555
            else:
              error_web[2]=200    
          except:
            error_web[2]=555

def web_trending():
          global config_sensor
          global historic_vars
          global buffer_web
          global error_web
          cant=len(historic_vars)
          if cant==0:
            return
          buffer_web.clear()
          buffer_web.append(config_sensor['user_rtu'])
          now = datetime.now()   
          dt_string = now.strftime("%Y-%m-%d")
          buffer_web.append(dt_string) 
          buffer_web.append(config_sensor['rtu_number']) 
          c=get_compresors()
          buffer_web.append(c) 
          buffer_web.append(cant)
          for i in range(cant):
            buffer_web.append(i) # Number of point
            buffer_web.append(historic_vars[i][0]) #VSD
            buffer_web.append(historic_vars[i][1]) #TCoil
            buffer_web.append(historic_vars[i][2]) #Spress1
            buffer_web.append(historic_vars[i][3]) #Spress2
            buffer_web.append(historic_vars[i][4]) #SHeat1
            buffer_web.append(historic_vars[i][5]) #SHeat2
            buffer_web.append(historic_vars[i][6]) #CO2
            buffer_web.append(historic_vars[i][7]) #TSpc
            buffer_web.append(historic_vars[i][8]) #time
          url='http://www.greenmediahd.com/rooftop/api_rtu_trend.php'
          try:
            rsp = requests.post(url, data=json.dumps(buffer_web) , timeout=4)
               #error_web.append(rsp.text)
            if rsp.status_code!=200:
              error_web[4]=566
            else:
              error_web[4]=200    
          except:
            error_web[4]=566

                
def web_iaq():
          global config_sensor
          global buffer_web
          global error_web
          buffer_web.clear()
          buffer_web.append(config_sensor['user_aqs'])
          now = datetime.now()   
          dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
          buffer_web.append(dt_string)
          buffer_web.append(version)
          buffer_web.append(1) #cantidad
          buffer_web.append(config_sensor['ip_add'])
          buffer_web.append(config_sensor['mac_iaq'])
          buffer_web.append("{:.0f}".format(sensor_values['score']))
          buffer_web.append("{:.0f}".format(sensor_values['temp']))
          buffer_web.append("{:.0f}".format(sensor_values['humid']))
          buffer_web.append("{:.0f}".format(sensor_values['co2']))
          buffer_web.append("{:.0f}".format(sensor_values['voc']))
          buffer_web.append("{:.0f}".format(sensor_values['pm25']))
          buffer_web.append("{:.0f}".format(sensor_values['error'])) #error
          url='http://greenmediahd.com/airdata/air_rtu_api.php'
          try:
            rsp = requests.post(url, data=json.dumps(buffer_web) , timeout=4)
            #error_web.append(rsp.text)
            error_web[1]=rsp.status_code
          except:
            error_web[1]=533
          if config_sensor['buffer_air_avail']>0:
            config_sensor['buffer_air_avail']=0
            web_iaq_buffer() #envia buffer de iaq a la nube

def web_iaq_buffer():
          global config_sensor
          global buffer_web
          global error_web
          global air_buffer
          buffer_web.clear()
          buffer_web.append(config_sensor['user_aqs'])
          
          day=config_sensor['buffer_air_year']
          buffer_web.append(day)
          day=config_sensor['buffer_air_month']
          buffer_web.append(day)
          day=config_sensor['buffer_air_day']
          buffer_web.append(day)
          
          for i in range(len(air_buffer)):
            for j in range(len(air_buffer[i])):
              buffer_web.append(air_buffer[i][j])
          url='http://greenmediahd.com/airdata/air_rtu_hist.php'
          try:
            rsp = requests.post(url, data=json.dumps(buffer_web) , timeout=10)
            #error_web.append(rsp.text)
            #error_web[3]=rsp.text
            error_web[3]=rsp.status_code
          except:
            error_web[3]=533
    

def start_web_task():
    global config_sensor
    if config_sensor['web_period']>0:
      t3 = threading.Thread(target=web_task, daemon=True)  
      t3.start()

def stop_web_task():
    global config_sensor
    global event_web
    if config_sensor['web_period']==0:
      event_web.set()
      time.sleep(1)
          
        
        
def air_sensor_task():
    global sensor_values
    global config_sensor
    global air_sampling
    global dynamic_web
    global event
    global dynamic_air
    while config_sensor['enabled']==1:
      if config_sensor['ip_add']!='':
        #case reboot failure in override
        if dynamic_air[0]<3:
           dynamic_air[0]=dynamic_air[0]+1
           if dynamic_air[0]==2:
              val_temp=0.0
              val_hum=0.0
              val_co2=0.0
              if config_sensor['override_co2']==1:
                  val_co2=3.0
              if config_sensor['override_temp']==1:
                  val_temp=3.0
              if config_sensor['override_hum']:
                  val_hum=3.0
              allGood=True
              if open_write_virtual()<0:
                  allGood=False  
              if set_value(144,val_co2)<0:
                    allGood=False          
              if set_value(139,val_temp)<0:
                    allGood=False          
              if set_value(142,val_hum)<0:
                    allGood=False          
              if save_virtual()<0:
                  allGood=False
              if open_read_virtual()<0:
                  allGood=False
        c=get_sensors(config_sensor)
        if "score" in c:
          if config_sensor['conv']>0:
            sensor_values['temp']=float("{:.1f}".format(c['temp']))
          else:  
            sensor_values['temp']=float("{:.1f}".format(c['temp'] * 1.8 + 32))
          #sensor_values['temp']=c['temp'] * 1.8 + 32
          sensor_values['humid']=float("{:.1f}".format(c['humid']))
          sensor_values['co2']=c['co2']
          if (sensor_values['co2']<400):
            sensor_values['co2']=400
          sensor_values['score']=c['score']
          sensor_values['voc']=c['voc']
          sensor_values['pm25']=c['pm25']
          sensor_values['error']=0
          if config_sensor['override_co2']==1:
            set_value(143,sensor_values['co2'])
          if config_sensor['override_temp']==1:
            set_value(138,sensor_values['temp'])
          if config_sensor['override_hum']==1:
            set_value(141,sensor_values['humid'])
        else:
          sensor_values['error']=1
        dynamic_web[2]=dynamic_web[2]-dynamic_web[1]
        if dynamic_web[2]<=0:
          dynamic_web[2]=10
          save_air_buffer()  
      event.wait(60)           
      #time.sleep(58)
    event.clear()

def start_air_sampling():
    global air_sampling
    global config_sensor
    if config_sensor['enabled']==1:
      air_sampling=True
      t2 = threading.Thread(target=air_sensor_task, daemon=True)  
      t2.start()

def stop_air_sampling():
    global air_sampling
    global config_sensor
    global event
    if config_sensor['enabled']==0:
      air_sampling=False
      event.set()
      time.sleep(1)
      
def make_conversion(vValue):
     global config_sensor
     if config_sensor['conv']>0:
        convertion=(vValue - 32) * 0.5556;
        return convertion
     else: 
      return vValue

init_vars(rtu_main_vars)
init_energy_vars(rtu_energy_vars)
init_alarm_vars(rtu_alarm_vars)
init_fail_vars(rtu_fail_vars)
init_setpoint_vars(rtu_setpoint_vars)
init_alarmlim_vars(rtu_alarmlim_vars)
init_sensorlim_vars(rtu_sensorlim_vars)
init_schedule_vars(rtu_schedule_vars)
init_general_vars(rtu_miscell_vars)
init_speedlim_vars(rtu_speedlim_vars)
init_sensors(sensor_values)
init_read_vars(rtu_read_vars)
init_write_vars(rtu_write_vars)
config_sensor=read_sensors()

t1 = threading.Thread(target=save_hist_buffer, daemon=True)  
t1.start()
event = threading.Event()
event_web = threading.Event()
start_air_sampling()
start_web_task()


from rtu_app import routes
