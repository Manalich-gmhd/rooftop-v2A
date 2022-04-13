from rtu_app.utility import get_value_syn,get_centigrade

def init_vars(rtu_main_vars):
      var = {}
      var['name']='Space Temp. Setpoint'    
      var['index']=159
      var['type']=0
      var['value']="0.0"
      var['unit']="oF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Space Temperature'    
      var['index']=168
      var['type']=0
      var['value']="0.0"
      var['unit']="oF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Carbon Dioxide (CO2)'    
      var['index']=145
      var['type']=0
      var['value']="0.0"
      var['unit']="ppm"
      rtu_main_vars.append(var)
      var = {}
      var['name']='VSD Hz'    
      var['index']=46
      var['type']=0
      var['value']="0.0"
      var['unit']="Hz"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Coil Temperature'    
      var['index']=6
      var['type']=0
      var['value']="0.0"
      var['unit']="oF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Refrigerant'    
      var['index']=22
      var['type']=13
      var['value']="R22"
      var['unit']=""
      rtu_main_vars.append(var)
      var = {}
      var['name']='Comp 1 Minutes'    
      var['index']=47
      var['type']=1
      var['value']="0"
      var['unit']="min"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Suction Press Comp 1'    
      var['index']=42
      var['type']=0
      var['value']="0.0"
      var['unit']="psi"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Refrig. Temp. Comp 1'    
      var['index']=18
      var['type']=10
      var['value']="0.0"
      var['unit']="oF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Suction Temp Comp 1'    
      var['index']=0
      var['type']=0
      var['value']="0.0"
      var['unit']="oF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Super-heat Comp 1'    
      var['index']=44
      var['type']=0
      var['value']="0.0"
      var['unit']="DoF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Heater 1'    
      var['index']=31
      var['type']=2
      var['value']="OFF"
      var['unit']=""
      rtu_main_vars.append(var)
      var = {}
      var['name']='Comp 2 Minutes'    
      var['index']=48
      var['type']=1
      var['value']="0"
      var['unit']="min"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Suction Press Comp 2'    
      var['index']=43
      var['type']=0
      var['value']="0.0"
      var['unit']="psi"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Refrig. Temp. Comp 2'    
      var['index']=19
      var['type']=10
      var['value']="0.0"
      var['unit']="oF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Suction Temp Comp 2'    
      var['index']=2
      var['type']=0
      var['value']="0.0"
      var['unit']="oF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Super-heat Comp 2'    
      var['index']=45
      var['type']=0
      var['value']="0.0"
      var['unit']="DoF"
      rtu_main_vars.append(var)
      var = {}
      var['name']='Heater 2'    
      var['index']=32
      var['type']=2
      var['value']="OFF"
      var['unit']=""
      rtu_main_vars.append(var)
      var = {}
      var['name']='Total Reset'
      var['index']=187
      var['type']=1
      var['value']="0"
      var['unit']=""
      rtu_main_vars.append(var)
      
def update_values(rtu_main_vars,conv=0):
   for i in range(len(rtu_main_vars)):
      if rtu_main_vars[i]['type']<10:
         rsp=get_value_syn(rtu_main_vars[i]['index'])
      else:
         rsp=get_value_syn(rtu_main_vars[i]['index'],1)
      if rsp is not None:
         if conv>0:
            if (rtu_main_vars[i]['unit']=="oF" or rtu_main_vars[i]['unit']=="oC"):
              rtu_main_vars[i]['unit']="oC"
              rsp=get_centigrade(rsp)
          #  elif (rtu_main_vars[i]['unit']=="DoF" or rtu_main_vars[i]['unit']=="DoC"):
          #      rtu_main_vars[i]['unit']="DoC"
          #      rsp=get_centigrade(rsp,1)
         else: 
            if rtu_main_vars[i]['unit']=="oC":
               rtu_main_vars[i]['unit']="oF"
          #  elif rtu_main_vars[i]['unit']=="DoC":
          #     rtu_main_vars[i]['unit']="DoF"
               
         if rtu_main_vars[i]['type']==0 or rtu_main_vars[i]['type']==10:
            rtu_main_vars[i]['value']="{:.1f}".format(rsp)
         elif rtu_main_vars[i]['type']==1 or rtu_main_vars[i]['type']==11:
            rtu_main_vars[i]['value']="{:.0f}".format(rsp)
         elif rtu_main_vars[i]['type']==2 or rtu_main_vars[i]['type']==12:
            if rsp==0:
               rtu_main_vars[i]['value']='OFF'
            else:
               rtu_main_vars[i]['value']='ON'   
         else:
            if rsp==1:
               rtu_main_vars[i]['value']='R22'
            elif rsp==2:
               rtu_main_vars[i]['value']='R410A'
            else:
               rtu_main_vars[i]['value']='R407C'
   
