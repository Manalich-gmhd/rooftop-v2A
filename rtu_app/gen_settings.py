from rtu_app.utility import get_value_syn,get_centigrade

def init_general_vars(rtu_general_vars):
      var = {}
      var['name']='Enable Speed Control'    
      var['index']=86
      var['type']=2
      var['value']="ON"
      var['step']="1"
      var['Min']="0"
      var['Max']="1"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Enable Schedule'    
      var['index']=87
      var['type']=2
      var['value']="OFF"
      var['step']="1"
      var['Min']="0"
      var['Max']="1"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Disconnect by Sensor Fail'    
      var['index']=121
      var['type']=2
      var['value']="OFF"
      var['step']="1"
      var['Min']="0"
      var['Max']="1"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Enable Evaluation'    
      var['index']=83
      var['type']=2
      var['value']="OFF"
      var['step']="1"
      var['Min']="0"
      var['Max']="1"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Occupancy Override'    
      var['index']=38
      var['type']=2
      var['value']="OFF"
      var['step']="1"
      var['Min']="0"
      var['Max']="1"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Enable heat/cool overlap'    
      var['index']=102
      var['type']=2
      var['value']="OFF"
      var['step']="1"
      var['Min']="0"
      var['Max']="1"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Fan Mode'    
      var['index']=156
      var['type']=4
      var['value']="Auto"
      var['step']="1"
      var['Min']="1"
      var['Max']="3"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Total Compressors'    
      var['index']=119
      var['type']=1
      var['value']="2"
      var['step']="1"
      var['Min']="1"
      var['Max']="2"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='RTU Mode'    
      var['index']=101
      var['type']=5
      var['value']="Auto"
      var['step']="1"
      var['Min']="0"
      var['Max']="2"
      var['unit']=""
      rtu_general_vars.append(var)
      var = {}
      var['name']='Suct Press 1 Offset'    
      var['index']=184
      var['type']=0
      var['value']="0.0"
      var['step']="1"
      var['Min']="-100"
      var['Max']="100"
      var['unit']="psi"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Suct Press 2 Offset'    
      var['index']=185
      var['type']=0
      var['value']="0.0"
      var['step']="1"
      var['Min']="-100"
      var['Max']="100"
      var['unit']="psi"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Fan Power'    
      var['index']=37
      var['type']=10
      var['value']="0.75"
      var['step']="0.05"
      var['Min']="0"
      var['Max']="22"
      var['unit']="kW"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Fan KW Proof'    
      var['index']=36
      var['type']=10
      var['value']="0.06"
      var['step']="0.01"
      var['Min']="0"
      var['Max']="2"
      var['unit']="kW"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Max Fan Sensor Volt'    
      var['index']=38
      var['type']=10
      var['value']="0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="10"
      var['unit']="volts"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Comp 1 Power'    
      var['index']=34
      var['type']=10
      var['value']="0"
      var['unit']="kW"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Comp 2 Power'    
      var['index']=35
      var['type']=10
      var['value']="0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="100"
      var['unit']="kW"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Suction Press Setpoint'    
      var['index']=20
      var['type']=10
      var['value']="110.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="600"
      var['unit']="psi"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Coil Temp Setpoint'    
      var['index']=21
      var['type']=10
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="80"
      var['unit']="oF"
      rtu_general_vars.append(var)
      var = {}
      var['name']='Refrigerant'    
      var['index']=22
      var['type']=13
      var['value']="R22"
      var['step']="1"
      var['Min']="1"
      var['Max']="3"
      var['unit']=""
      rtu_general_vars.append(var)
      
      
def update_general_values(rtu_general_vars, conv=0):
   for i in range(len(rtu_general_vars)):
      if rtu_general_vars[i]['type']<10:
         rsp=get_value_syn(rtu_general_vars[i]['index'])
      else:
         rsp=get_value_syn(rtu_general_vars[i]['index'],1)
      if rsp is not None:
         if conv>0:
            if (rtu_general_vars[i]['unit']=="oF" or rtu_general_vars[i]['unit']=="oC"):
               rtu_general_vars[i]['unit']="oC"
               rsp=get_centigrade(rsp) 
         else:
            if rtu_general_vars[i]['unit']=="oC":
               rtu_general_vars[i]['unit']="oF"
         
         if rtu_general_vars[i]['type']==0 or rtu_general_vars[i]['type']==10:
            rtu_general_vars[i]['value']="{:.2f}".format(rsp)
         elif rtu_general_vars[i]['type']==1 or rtu_general_vars[i]['type']==11:
            rtu_general_vars[i]['value']="{:.0f}".format(rsp)
         elif rtu_general_vars[i]['type']==2 or rtu_general_vars[i]['type']==12:
            if rsp==0:
               rtu_general_vars[i]['value']='OFF'
            else:
               rtu_general_vars[i]['value']='ON'  
         elif rtu_general_vars[i]['type']==4: 
            if rsp==2:
               rtu_general_vars[i]['value']='Continuous'
            else:
               rtu_general_vars[i]['value']='Auto'  
         elif rtu_general_vars[i]['type']==5: 
            if rsp>1:
               rtu_general_vars[i]['value']='Heating'
            else:
               if rsp==1:
                  rtu_general_vars[i]['value']='Cooling'
               else:
                  rtu_general_vars[i]['value']='Auto'  

         else:
            if rsp==1:
               rtu_general_vars[i]['value']='R22'
            elif rsp==2:
               rtu_general_vars[i]['value']='R410A'
            else:
               rtu_general_vars[i]['value']='R407C'
   
