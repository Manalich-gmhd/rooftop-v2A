from rtu_app.utility import get_value_syn,get_centigrade

def init_setpoint_vars(setpoint_list):
      var = {}
      var['name']='Occ. Space Temp Cool SP'    
      var['index']=40
      var['type']=0
      var['value']="0.00"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="85"
      var['unit']="oF"
      setpoint_list.append(var)
      var = {}
      var['name']='Occ. Space Temp Heat SP'    
      var['index']=41
      var['type']=0
      var['value']="0.00"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="67"
      var['unit']="oF"
      setpoint_list.append(var)
      var = {}
      var['name']='Unocc. Space Temp Cool SP'    
      var['index']=149
      var['type']=0
      var['value']="0.00"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="90"
      var['unit']="oF"
      setpoint_list.append(var)
      var = {}
      var['name']='Unocc. Space Temp Heat SP'    
      var['index']=148
      var['type']=0
      var['value']="0.00"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="63"
      var['unit']="oF"
      setpoint_list.append(var)      
      var = {}
      var['name']='CO2 Set Point'    
      var['index']=161
      var['type']=0
      var['value']="0.00"
      var['step']="1"
      var['Min']="0"
      var['Max']="1500"
      var['unit']="ppm"
      setpoint_list.append(var)
      
def update_setpoint(setpoint_list,conv=0):
   for i in range(len(setpoint_list)):
      if setpoint_list[i]['type']<10:
         rsp=get_value_syn(setpoint_list[i]['index'])
      else:
         rsp=get_value_syn(setpoint_list[i]['index'],1)
      if rsp is not None:  
         
         if conv>0:
            if (setpoint_list[i]['unit']=="oF" or setpoint_list[i]['unit']=="oC"):
               setpoint_list[i]['unit']="oC"
               rsp=get_centigrade(rsp)
         else:
            if setpoint_list[i]['unit']=="oC":
               setpoint_list[i]['unit']="oF"
          
         if setpoint_list[i]['type']==0 or setpoint_list[i]['type']==10:
            setpoint_list[i]['value']="{:.1f}".format(rsp)
         elif setpoint_list[i]['type']==1 or setpoint_list[i]['type']==11:
            setpoint_list[i]['value']="{:.0f}".format(rsp)
                  
      