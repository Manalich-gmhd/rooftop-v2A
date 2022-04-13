from flask import render_template, request, redirect, url_for, flash, make_response
from rtu_app import app, rtu_main_vars,rtu_energy_vars,rtu_alarm_vars,rtu_fail_vars,rtu_setpoint_vars,rtu_alarmlim_vars,rtu_sensorlim_vars,rtu_schedule_vars,rtu_miscell_vars,rtu_speedlim_vars,historic_vars,config_sensor,sensor_values,air_sampling,start_air_sampling,stop_air_sampling,rtu_read_vars,buffer_web,error_web,start_web_task,stop_web_task,air_buffer,web_check,dynamic_air
from functools import wraps 
import re
import xml.etree.ElementTree as et
#from basMeg import Platform
#from basMeg import Device
from rtu_app.utility import set_value,open_write_webv,save_webv,open_read_webv,open_write_virtual,set_initial_virtual,save_virtual,open_read_virtual,reset_energy,get_evaluation,get_compresors,get_fahrenheit,get_emergency
from rtu_app.schedule import  update_schedule,get_schedule_enable
from rtu_app.alarm import update_alarm
from rtu_app.alarm_limits import update_alarm_lim
from rtu_app.gen_settings import update_general_values
from rtu_app.sensor_limit import update_sensor_lim
from rtu_app.sensor_fail import update_fail
from rtu_app.setpoint import update_setpoint
from rtu_app.energy import update_energy
from rtu_app.main import update_values
from rtu_app.speed_limit import update_speed_lim
from rtu_app.air_sensor import read_sensors,write_sensors,get_sensors
import threading
import socket
#import asyncio
#import aiohttp
import json
#from aiohttp_requests import requests

jsonstr=""

def get_ip():
    """Pirated from the interweb"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip
 
def auth_required_info(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'admin' and (auth.password == 'GMHD' or auth.password == 'adminGMHD') :
            return f(*args, **kwargs)

        return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated
      
def auth_required_modify(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if auth and auth.username == 'admin' and  auth.password == 'adminGMHD' :
            return f(*args, **kwargs)

        return make_response('Could not verify your login!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

    return decorated
      
#async def get_var_io(sIpAddress,iIndex):
#   url='http://' + sIpAddress + '/cgi-bin/xml-cgi'
#   data='<rdom fcn="get" doc="rtd" path="obj[' + str(iIndex) + ']/val_scl"/>'
#   async with aiohttp.ClientSession() as session:
#        async with session.post(url, data=data) as response:
#            data = await response.text()
#            return data


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r
   
@app.errorhandler(404)
  
# inbuilt function which takes error as parameter
def not_found(e):
# defining function
  return render_template("404.html")

@app.route("/get_values")
def get_values():
    global config_sensor
    update_values(rtu_main_vars,config_sensor['conv'])
    list_val=[rtu_main_vars[i]['value'] for i in range(len(rtu_main_vars)) ]
    return json.dumps(list_val)
 
@app.route("/get_energy_values")
def get_energy_values():
    update_energy(rtu_energy_vars)
    list_val=[rtu_energy_vars[i]['value'] for i in range(len(rtu_energy_vars)) ]
    return json.dumps(list_val)
      
@app.route("/get_alarm_values")
def get_alarm_values():
    update_alarm(rtu_alarm_vars,False)
    list_val=[rtu_alarm_vars[i]['value'] for i in range(len(rtu_alarm_vars)) ]
    return json.dumps(list_val)
   
@app.route("/get_fail_values")
def get_fail_values():
    update_fail(rtu_fail_vars,False)
    list_val=[rtu_fail_vars[i]['value'] for i in range(len(rtu_fail_vars)) ]
    return json.dumps(list_val)

@app.route("/reset_energy_values")
def reset_energy_values():
    reset_energy()
    return "[200]"

@app.route("/get_historic")
def get_historic():
    #update_buffer(historic_vars)
    return json.dumps(historic_vars)
 
 
#TEST------quitar##################################
@app.route("/get_buffer")
def get_buffer():
   #return f"Valor Dinamico {dynamic_web}"
   #return json.dumps(dynamic_web)
   #web_iaq_buffer()
   return json.dumps(buffer_web)

@app.route("/get_air_buffer")
def get_air_buffer():
   #return f"Valor Dinamico {dynamic_web}"
   #return json.dumps(dynamic_web)
   #web_iaq_buffer()
   return json.dumps(air_buffer)

@app.route("/get_error")
def get_error():
   return json.dumps(dynamic_air) 

@app.route("/get_check")
def get_check():
  # save_air_buffer()
   c=web_check()
   return json.dumps(c) 


@app.route("/get_sensor")
def get_sensor():
    c=get_sensors(config_sensor)
    if "score" in c:
      return json.dumps(c)
    else:
      return 'ERROR'

@app.route("/read_conf")
def read_conf():
    return json.dumps(config_sensor)

################################

   
@app.route("/read_sensor")
def read_sensor():
    return json.dumps(sensor_values)

@app.route("/config_web_values")
@auth_required_modify
def config_web_values():
    return render_template('setup_web.html',config=config_sensor,error=error_web)


@app.route("/config_values")
@auth_required_modify
def config_values():
    return render_template('config.html',config=config_sensor)

@app.route("/air_sensors")
@auth_required_info
def air_sensors():
    return render_template('air_sensor.html',sensor=sensor_values,err=sensor_values['error'])

@app.context_processor
def context_processor():
    return dict(conf=config_sensor)

@app.route("/")
@auth_required_info
def index():
    global config_sensor
    emer=get_emergency()
    update_values(rtu_main_vars,config_sensor['conv'])
    return render_template('index.html',datos=rtu_main_vars, em=emer)
   
@app.route("/alarm")
@auth_required_info
def alarm():
    global config_sensor
    update_alarm(rtu_alarm_vars,True,config_sensor['conv']),
    return render_template('alarm.html',datos=rtu_alarm_vars)

@app.route("/sensor")
@auth_required_info
def sensor():
    global config_sensor
    update_fail(rtu_fail_vars,True,config_sensor['conv'])
    return render_template('sensor_fail.html',datos=rtu_fail_vars)
   
#   ipAddress='192.168.1.22'
#   bc = Device(ipAddress)
   # Error?
#   if bc.ePlatform == Platform.BASC_NONE:
#      return 'Unable to connect with RTC-SC'
#   result = bc.universalInput(1)
#   return f'Value {result}'

@app.route("/schedules")
@auth_required_modify
def schedules():
    update_schedule(rtu_schedule_vars)
    ena=get_schedule_enable()
    return render_template('schedule.html',datos=rtu_schedule_vars,en_sc=ena)
    #return render_template('schedule.html')
    #jsonstr=json.dumps(rtu_schedule_vars)
    #return jsonstr
 
@app.route("/trending")
@auth_required_info
def trending():
    c=get_compresors();
    return render_template('trending.html',comp=c)
 
 
@app.route("/setpoints")
@auth_required_modify
def setpoints():
    global config_sensor
    update_setpoint(rtu_setpoint_vars,config_sensor['conv'])
    return render_template('setpoint.html',datos=rtu_setpoint_vars)
   
@app.route("/energy")
@auth_required_info
def energy():
    update_energy(rtu_energy_vars)
    eva=get_evaluation()
#    return f"Evaluation {eva}"
    return render_template('energy.html',datos=rtu_energy_vars,evalua=eva)
#   loop = asyncio.new_event_loop()
#   text = loop.run_until_complete(get_var_io("192.168.1.22",0))
#   return f"Energy Saving {text}"

@app.route("/alarm_limit")
@auth_required_modify
def alarm_limit():
    global config_sensor
    update_alarm_lim(rtu_alarmlim_vars,config_sensor['conv'])
    return render_template('alarm_limits.html',datos=rtu_alarmlim_vars)

@app.route("/sensor_limit")
@auth_required_modify
def sensor_limit():
    global config_sensor   
    update_sensor_lim(rtu_sensorlim_vars,config_sensor['conv'])
    return render_template('sensor_limits.html',datos=rtu_sensorlim_vars)
 
@app.route("/speed_limit")
@auth_required_modify
def speed_limit():
    update_speed_lim(rtu_speedlim_vars)
    return render_template('speed_limits.html',datos=rtu_speedlim_vars)
 
@app.route("/miscell_values")
@auth_required_modify
def miscell_values():
    global config_sensor
    update_general_values(rtu_miscell_vars,config_sensor['conv'])
    return render_template('gen_settings.html',datos=rtu_miscell_vars)
           

@app.route("/controller")
def controller():
      ip=get_ip()
      return redirect("http://"+ip)
      
@app.route("/config")
def config():
    update_energy(rtu_energy_vars)
    jsonstr=json.dumps(rtu_energy_vars)
    return jsonstr
 

@app.route('/write_alarmlim', methods=['POST'])
def write_alarmlim():
    global config_sensor
    if request.method == 'POST':
       allGood=True
       if open_write_virtual()<0:
          allGood=False
       for i in range(len(rtu_alarmlim_vars)):
         value_sp=float(request.form['val_'+str(i+1)])
         if config_sensor['conv']>0:
              if (rtu_alarmlim_vars[i]['unit']=="oC"):
               value_sp=get_fahrenheit(value_sp)

         if set_initial_virtual(rtu_alarmlim_vars[i]['index'],value_sp)<0:
            allGood=False
         if set_value(rtu_alarmlim_vars[i]['index'],value_sp)<0:
            allGood=False
       if save_virtual()<0:
          allGood=False
       if open_read_virtual()<0:
          allGood=False
       if allGood:     
         flash('Alarm Limits modified successfully','success')
       else:
         flash('Some error trying to change Alarm Limits','warning')
       config_sensor['send_command']=1  
    return redirect(url_for('alarm_limit'))

@app.route('/write_speedlim', methods=['POST'])
def write_speedlim():
    global config_sensor
    if request.method == 'POST':
       allGood=True
       if open_write_virtual()<0:
          allGood=False
       for i in range(len(rtu_speedlim_vars)):
         if set_initial_virtual(rtu_speedlim_vars[i]['index'],float(request.form['val_'+str(i+1)]))<0:
            allGood=False
         if set_value(rtu_speedlim_vars[i]['index'],float(request.form['val_'+str(i+1)]))<0:
            allGood=False
       if save_virtual()<0:
          allGood=False
       if open_read_virtual()<0:
          allGood=False
       if allGood:     
         flash('Fan Speed Limits modified successfully','success')
       else:
         flash('Some error trying to change Fan Speed Limits','warning')
       config_sensor['send_command']=1  
    return redirect(url_for('speed_limit'))


@app.route('/write_schedule', methods=['POST'])
def write_schedule():
    global config_sensor
    if request.method == 'POST':
       allGood=True
       if open_write_virtual()<0:
          allGood=False
       for i in range(len(rtu_schedule_vars)):
         v1=request.form['timeOn_'+str(i)][:2];
         v2=request.form['timeOn_'+str(i)][3:];
         v3=request.form['timeOff_'+str(i)][:2];
         v4=request.form['timeOff_'+str(i)][3:];
         if set_initial_virtual(rtu_schedule_vars[i]['index_hon'],float(v1))<0:
              allGood=False       
         if set_value(rtu_schedule_vars[i]['index_hon'],float(v1))<0:
              allGood=False       
         if set_initial_virtual(rtu_schedule_vars[i]['index_mon'],float(v2))<0:
              allGood=False       
         if set_value(rtu_schedule_vars[i]['index_mon'],float(v2))<0:
              allGood=False       
         if set_initial_virtual(rtu_schedule_vars[i]['index_hoff'],float(v3))<0:
              allGood=False       
         if set_value(rtu_schedule_vars[i]['index_hoff'],float(v3))<0:
              allGood=False       
         if set_initial_virtual(rtu_schedule_vars[i]['index_moff'],float(v4))<0:
              allGood=False       
         if set_value(rtu_schedule_vars[i]['index_moff'],float(v4))<0:
              allGood=False       
#       return f"Valor de wk {v1} and {v2}"
       if save_virtual()<0:
          allGood=False
       if open_read_virtual()<0:
          allGood=False
       if allGood:     
         flash('Schedules modified successfully','success')
       else:
         flash('Some error trying to change Schedules','warning')
       config_sensor['send_command']=1  
    return redirect(url_for('schedules'))


@app.route('/write_sensorlim', methods=['POST'])
def write_sensorlim():
    global config_sensor
    if request.method == 'POST':
       allGood=True
       if open_write_virtual()<0:
          allGood=False
       for i in range(len(rtu_sensorlim_vars)):
         value_sp=float(request.form['val_'+str(i+1)])
         if config_sensor['conv']>0:
              if (rtu_sensorlim_vars[i]['unit']=="oC"):
               value_sp=get_fahrenheit(value_sp)
          
         if set_initial_virtual(rtu_sensorlim_vars[i]['index'],value_sp)<0:
            allGood=False
         if set_value(rtu_sensorlim_vars[i]['index'],value_sp)<0:
            allGood=False
       if save_virtual()<0:
          allGood=False
       if open_read_virtual()<0:
          allGood=False
       if allGood:     
         flash('Sensor Limits modified successfully','success')
       else:
         flash('Some error trying to change Sensor Limits','warning')
       config_sensor['send_command']=1  
    return redirect(url_for('sensor_limit'))

 
@app.route('/write_sepoints', methods=['POST'])
def write_sepoints():
    global config_sensor
    if request.method == 'POST':
       #rval=[]
       allGood=True
       if open_write_virtual()<0:
          allGood=False
       for i in range(len(rtu_setpoint_vars)):
         #indexI='val_'+str(i)
         #rval.append(float(request.form[indexI]))
         value_sp=float(request.form['val_'+str(i+1)])
         if config_sensor['conv']>0:
              if (rtu_setpoint_vars[i]['unit']=="oC"):
               value_sp=get_fahrenheit(value_sp)

         if set_initial_virtual(rtu_setpoint_vars[i]['index'],value_sp)<0:
            allGood=False
         if set_value(rtu_setpoint_vars[i]['index'],value_sp)<0:
            allGood=False
       if save_virtual()<0:
          allGood=False
       if open_read_virtual()<0:
          allGood=False
       if allGood:     
         flash('Setpoints modified successfully','success')
       else:
         flash('Some error trying to change Setpoints','warning')
       config_sensor['send_command']=1       
    return redirect(url_for('setpoints'))

       #jsonstr=json.dumps(rval)
       #return jsonstr         

      #  fullname = request.form['fullname']
      #  phone = request.form['phone']
      #  flash('Setpoints modified successfully')
      #  return redirect(url_for('setpoints'))

# Define a function for
# validate an Ip address
def check(Ip):
    regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, Ip)):
        return True
         
    else:
        return False

@app.route('/write_config', methods=['POST'])
def write_config():
   global config_sensor
   est_init=config_sensor['enabled']
   if request.method == 'POST':
      if not check(request.form['ip_add']):
         flash('Invalid IP Adrress ','danger')
         return redirect(url_for('config_values'))
      if int(request.form['port'])<80:
         flash('Invalid Port ','danger')
         return redirect(url_for('config_values'))
      config_sensor['ip_add']=request.form['ip_add']
      config_sensor['port']=int(request.form['port'])
      val_temp=0.0
      val_hum=0.0
      val_co2=0.0
      if 'enabled' in request.form:
         config_sensor['enabled']=1
      else:
         config_sensor['enabled']=0         
      if 'override_co2' in request.form:
         config_sensor['enabled']=1
         val_co2=3.0
         config_sensor['override_co2']=1
      else:
         config_sensor['override_co2']=0         
      if 'override_temp' in request.form:
         val_temp=3.0
         config_sensor['enabled']=1
         config_sensor['override_temp']=1
      else:
         config_sensor['override_temp']=0         
      if 'override_hum' in request.form:
         val_hum=3.0
         config_sensor['enabled']=1
         config_sensor['override_hum']=1
      else:
         config_sensor['override_hum']=0         
      write_sensors(config_sensor)
      if (est_init==0)and(config_sensor['enabled']==1):
         start_air_sampling()
      elif (est_init==1)and(config_sensor['enabled']==0):
         stop_air_sampling()
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
      if allGood:     
         flash('Values modified successfully','success')
      else:
         flash('Some errors trying to set Overrides','warning')
      
      return redirect(url_for('config_values'))
      
     # return json.dumps(config_sensor)


@app.route('/write_web_config', methods=['POST'])
def write_web_config():
   global config_sensor
   est_init=config_sensor['web_period']
   if request.method == 'POST':
      config_sensor['user_rtu']=int(request.form['user_rtu'])
      config_sensor['user_aqs']=int(request.form['user_aqs'])
      config_sensor['web_period']=int(request.form['web_period'])
      config_sensor['rtu_number']=int(request.form['rtu_number'])
      config_sensor['total_rtus']=int(request.form['total_rtus'])
      config_sensor['trend_opc']=int(request.form['trend_opc'])
      write_sensors(config_sensor)
      if (est_init==0)and(config_sensor['web_period']>0):
         start_web_task()
      elif (est_init>0)and(config_sensor['web_period']==0):
         stop_web_task()
      flash('Values modified successfully','success')
      return redirect(url_for('config_web_values'))
      
     # return json.dumps(config_sensor)

@app.route('/write_units', methods=['POST'])
def write_units():
    global config_sensor
    global historic_vars
    if request.method == 'POST':
       val_conv=int(request.form['val_conv'])
       historic_vars.clear()
       config_sensor['conv']=val_conv
       write_sensors(config_sensor)
    return redirect(url_for('miscell_values'))


@app.route('/write_miscell', methods=['POST'])
def write_miscell():
    global config_sensor
    if request.method == 'POST':
       #rval=[]
      # val_conv=int(request.form['val_conv'])
      # config_sensor['conv']=val_conv
      # write_sensors(config_sensor)
       
       last_i=0
       #valueform=""
       allGood=True
       #  return request.form
       if open_write_virtual()<0:
          allGood=False
       for i in range(0,11):
             if i >= 6:
                #valueform=request.form['val_'+str(i+1)]
                if set_initial_virtual(rtu_miscell_vars[i]['index'],float(request.form['val_'+str(i+1)]))<0:
                   allGood=False
                if set_value(rtu_miscell_vars[i]['index'],float(request.form['val_'+str(i+1)]))<0:
                   allGood=False
                   last_i=i
             elif 'val_'+str(i+1) in request.form:
                   if set_initial_virtual(rtu_miscell_vars[i]['index'],1)<0:
                      allGood=False
                   if set_value(rtu_miscell_vars[i]['index'],1)<0:
                      allGood=False
             else:
                   if set_initial_virtual(rtu_miscell_vars[i]['index'],0)<0:
                      allGood=False
                   if set_value(rtu_miscell_vars[i]['index'],0)<0:
                      allGood=False
                      last_i=i
                #rval.append('Val '+str(i+1)+' is OFF') 
       if save_virtual()<0:
          allGood=False
       if open_read_virtual()<0:
          allGood=False
                   
       # save web variables               
       if open_write_webv()<0:
             allGood=False
             last_i=33
                      
       for i in range(11,len(rtu_miscell_vars)):
             value_sp=float(request.form['val_'+str(i+1)])
             if config_sensor['conv']>0:
                  if (rtu_miscell_vars[i]['unit']=="oC"):
                     value_sp=get_fahrenheit(value_sp)
          
             if set_value(rtu_miscell_vars[i]['index'],value_sp,1)<0:
                allGood=False
             #if i == 15:
             #   if set_value(rtu_miscell_vars[i]['index'],float(request.form['val_'+str(i+1)]),1)<0:
              #     allGood=False
       if save_webv()<0:
          allGood=False
       if open_read_webv()<0:
          allGood=False
          
       if allGood:     
         flash('Values modified successfully','success')
       else:
         flash('Some error trying to change values','warning')
       config_sensor['send_command']=1  
    return redirect(url_for('miscell_values'))
      
#       jsonstr=json.dumps(rval)
#       return jsonstr         
                
   
   
    #return request.form

