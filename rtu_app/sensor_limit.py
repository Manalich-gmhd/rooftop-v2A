from rtu_app.utility import get_value_syn,get_centigrade

def init_sensorlim_vars(sensorlim_list):
      var = {}
      var['name']='Coil Temp. Low Lim. C_OFF'
      var['index']=115
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Coil Temp. High Lim. C_OFF'
      var['index']=116
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0" 
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Coil Temp. Low Lim. C_ON'
      var['index']=117
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Coil Temp. High Lim. C_ON'
      var['index']=118
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Temp. Low Lim. C_OFF'
      var['index']=111
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Temp. High Lim. C_OFF'
      var['index']=112
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0" 
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Temp. Low Lim. C_ON'
      var['index']=113
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Temp. High Lim. C_ON'
      var['index']=114
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      var['unit']="oF"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Press. Low Lim. C_OFF'
      var['index']=107
      var['value']="0.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="500"
      var['unit']="psi"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Press. High Lim. C_OFF'
      var['index']=108
      var['value']="0.0"
      var['step']="1"
      var['Min']="0" 
      var['Max']="500"
      var['unit']="psi"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Press. Low Lim. C_ON'
      var['index']=109
      var['value']="0.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="500"
      var['unit']="psi"
      sensorlim_list.append(var)
      var = {}
      var['name']='Suction Press. High Lim. C_ON'
      var['index']=110
      var['value']="0.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="500"
      var['unit']="psi"
      sensorlim_list.append(var)

def update_sensor_lim(sensorlim_list,conv=0):
   for i in range(len(sensorlim_list)):
      rsp=get_value_syn(sensorlim_list[i]['index'])
      if rsp is not None:
         if conv>0:
            if (sensorlim_list[i]['unit']=="oF" or sensorlim_list[i]['unit']=="oC"):
               sensorlim_list[i]['unit']="oC"
               rsp=get_centigrade(rsp)
         else:
            if sensorlim_list[i]['unit']=="oC":
               sensorlim_list[i]['unit']="oF"
            
         sensorlim_list[i]['value']="{:.1f}".format(rsp)
   
