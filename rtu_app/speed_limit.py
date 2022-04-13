from rtu_app.utility import get_value_syn

def init_speedlim_vars(lim_list):
      var = {}
      var['name']='Fan Only Mode Speed'
      var['index']=106
      var['value']="15.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="60"
      var['unit']="Hz"
      lim_list.append(var)
      var = {}
      var['name']='One Compressor Min. Speed'
      var['index']=81
      var['value']="25.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="60"
      var['unit']="Hz"
      lim_list.append(var)
      var = {}
      var['name']='Two Compressors Min. Speed'
      var['index']=82
      var['value']="35.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="60"
      var['unit']="Hz"
      lim_list.append(var)
      var = {}
      var['name']='Heating Speed'
      var['index']=85
      var['value']="52.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="60"
      var['unit']="Hz"
      lim_list.append(var)
      var = {}
      var['name']='Start Speed'
      var['index']=84
      var['value']="40.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="60"
      var['unit']="Hz"
      lim_list.append(var)
      var = {}
      var['name']='CO2 Speed Override'    
      var['index']=178
      var['type']=0
      var['value']="30.00"
      var['step']="1"
      var['Min']="0"
      var['Max']="60"
      var['unit']="Hz"
      lim_list.append(var)
      var = {}
      var['name']='Max VSD Speed'    
      var['index']=183
      var['type']=0
      var['value']="60.00"
      var['step']="1"
      var['Min']="0"
      var['Max']="60"
      var['unit']="Hz"
      lim_list.append(var)
      

def update_speed_lim(lim_list):
   for i in range(len(lim_list)):
      rsp=get_value_syn(lim_list[i]['index'])
      if rsp is not None:
            lim_list[i]['value']="{:.0f}".format(rsp)
   
