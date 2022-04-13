from rtu_app.utility import get_value_syn

def init_energy_vars(energy_list):
      var = {}
      var['name']='60 Hz Fan Power'    
      var['index']=65
      var['type']=0
      var['value']="0.00"
      var['unit']="kW"
      energy_list.append(var)
      var = {}
      var['name']='Compresor Power'    
      var['index']=34 
      var['type']=10
      var['value']="0.00"
      var['unit']="kW"
      energy_list.append(var)
      var = {}
      var['name']='Fan Current Power'    
      var['index']=64
      var['type']=0
      var['value']="0.0"
      var['unit']="kW"
      energy_list.append(var)
      var = {}
      var['name']='Fan YTD Savings %'    
      var['index']=74
      var['type']=0
      var['value']="0.0"
      var['unit']="%"
      energy_list.append(var)
      var = {}
      var['name']='Fan kWh Savings YTD'    
      var['index']=75
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh"
      energy_list.append(var)
      var = {}
      var['name']='Total kWh Reduction YTD'    
      var['index']=70
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh"
      energy_list.append(var)
      var = {}
      var['name']='Ave. kWh Run Hour Reduction'    
      var['index']=71
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh"
      energy_list.append(var)
      var = {}
      var['name']='RTU kWh'    
      var['index']=77
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh"
      energy_list.append(var)
      var = {}
      var['name']='RTU Average Kwh per Hour'    
      var['index']=72
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh"
      energy_list.append(var)
      var = {}
      var['name']='Fan Kw Reduction'    
      var['index']=67
      var['type']=0
      var['value']="0.0"
      var['unit']="kW"
      energy_list.append(var)
      var = {}
      var['name']='Compressor Kw Reduction'    
      var['index']=68
      var['type']=0
      var['value']="0.0"
      var['unit']="kW"
      energy_list.append(var)
      var = {}
      var['name']='Total Kw Reduction'    
      var['index']=69
      var['type']=0
      var['value']="0.0"
      var['unit']="kW"
      energy_list.append(var)
      var = {}
      var['name']='RTU Kw'    
      var['index']=73
      var['type']=0
      var['value']="0.0"
      var['unit']="kW"
      energy_list.append(var)
      var = {}
      var['name']='Fan Run Hours'    
      var['index']=78
      var['type']=0
      var['value']="0.0"
      var['unit']="hours"
      energy_list.append(var)
      var = {}
      var['name']='Comp. 1 Run Hours'    
      var['index']=79
      var['type']=0
      var['value']="0.0"
      var['unit']="hours"
      energy_list.append(var)
      var = {}
      var['name']='Comp. 2 Run Hours'    
      var['index']=80
      var['type']=0
      var['value']="0.0"
      var['unit']="hours" 
      energy_list.append(var)
      var = {}
      var['name']='Total Even Days kWh'    
      var['index']=162
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh" 
      energy_list.append(var)
      var = {}
      var['name']='Total Odd Days kWh'    
      var['index']=163
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh" 
      energy_list.append(var)
      var = {}
      var['name']='Total Even Days'    
      var['index']=164
      var['type']=0
      var['value']="0.0"
      var['unit']="" 
      energy_list.append(var)
      var = {}
      var['name']='Total Odd Days'    
      var['index']=165
      var['type']=0
      var['value']="0.0"
      var['unit']="" 
      energy_list.append(var)
      var = {}
      var['name']='Average kWh Saved (AO-AE)'    
      var['index']=166
      var['type']=0
      var['value']="0.0"
      var['unit']="kWh" 
      energy_list.append(var)
      var = {}
      var['name']='Eval. Saving Percent'    
      var['index']=177
      var['type']=0
      var['value']="0.0"
      var['unit']="%" 
      energy_list.append(var)


def update_energy(energy_list):
   for i in range(len(energy_list)):
      if energy_list[i]['type']<10:
         rsp=get_value_syn(energy_list[i]['index'])
      else:
         rsp=get_value_syn(energy_list[i]['index'],1)
      if rsp is not None:
         if energy_list[i]['type']==0 or energy_list[i]['type']==10:
            energy_list[i]['value']="{:.3f}".format(rsp)
         elif energy_list[i]['type']==1 or energy_list[i]['type']==11:
            energy_list[i]['value']="{:.0f}".format(rsp)
   
