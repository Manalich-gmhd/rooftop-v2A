import json
import requests
from rtu_app.utility import open_write_virtual,set_value,save_virtual,open_read_virtual

def read_sensors():
    config={}
    config['ip_add']=''
    config['port']=80
    config['override_co2']=0
    config['override_temp']=0
    config['override_hum']=0
    config['enabled']=0
    config['user_rtu']=0
    config['user_aqs']=0
    config['web_period']=0
    config['rtu_number']=1
    config['total_rtus']=1
    config['send_command']=0
    config['force_upload']=0
    config['mac_iaq']=''
    config['buffer_air_day']=0
    config['buffer_air_avail']=0
    config['last_upload']=''
    config['buffer_air_month']=0
    config['buffer_air_year']=0
    config['conv']=0
    config['trend_opc']=0
    error=False

    try:
        with open('config.json', 'r') as fp:
            config = json.load(fp)
    except:
        error=True
    val_temp=0.0
    val_hum=0.0
    val_co2=0.0
    if config['override_co2']==1:
        config['enabled']=1
        val_co2=3.0
    if config['override_temp']==1:
        val_temp=3.0
        config['enabled']=1
    if config['override_hum']:
        val_hum=3.0
        config['enabled']=1
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
    return  config       

        #airsensor ={'ip_add':'','port':80,'control_co2':0}
#    return airsensor    

def write_sensors(config_sensor):
    with open('config.json', 'w') as fp:
        json.dump(config_sensor, fp)
        

def get_sensors(config_sensor):
    ip=config_sensor['ip_add']
    port=config_sensor['port']
    url='http://' + ip + ':'+str(port)+ '/air-data/latest'
    url_mac='http://' + ip + ':'+str(port)+ '/settings/config/data'
    error={'error':1}
    me=0
#    return url
    try:
      rsp = requests.get(url_mac, timeout=2)
      if (rsp.status_code == 200):
        c=rsp.json()
        config_sensor['mac_iaq']=c['wifi_mac']
    except:
      me=1      

    try:
      rsp = requests.get(url, timeout=2)
      if (rsp.status_code == 200):
        sensors=rsp.json()
        return sensors
      else:
        return error
    except:
        return error
#    return error   
  
def init_sensors(sensor_values):
    sensor_values['temp']=0
    sensor_values['humid']=0
    sensor_values['co2']=0
    sensor_values['score']=0
    sensor_values['voc']=0
    sensor_values['pm25']=0
    sensor_values['error']=0
   

