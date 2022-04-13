from rtu_app.utility import get_value_syn,get_centigrade

def init_alarmlim_vars(alarmlim_list):
      var = {}
      var['name']='High Coil Temp.'
      var['index']=127
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="0"
      var['Max']="80"
      var['unit']="oF"
      alarmlim_list.append(var)
      var = {}
      var['name']='Low Suct. Press.'
      var['index']=123
      var['value']="0.0"
      var['step']="1"
      var['Min']="0" 
      var['Max']="400"
      var['unit']="psi"
      alarmlim_list.append(var)
      var = {}
      var['name']='High Suct. Press.'
      var['index']=124
      var['value']="0.0"
      var['step']="1"
      var['Min']="0"
      var['Max']="400"
      var['unit']="psi"
      alarmlim_list.append(var)
      var = {}
      var['name']='Low Superheat'
      var['index']=125
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="1"
      var['Max']="100"
      var['unit']="DoF"
      alarmlim_list.append(var)
      var = {}
      var['name']='High Superheat'
      var['index']=126
      var['value']="0.0"
      var['step']="0.1"
      var['Min']="1"
      var['Max']="100"
      var['unit']="DoF"
      alarmlim_list.append(var)

def update_alarm_lim(alarmlim_list,conv=0):
   for i in range(len(alarmlim_list)):
      rsp=get_value_syn(alarmlim_list[i]['index'])
      if rsp is not None:
            if conv>0:
                  if (alarmlim_list[i]['unit']=="oF" or alarmlim_list[i]['unit']=="oC"):
                        alarmlim_list[i]['unit']="oC"
                        rsp=get_centigrade(rsp)
                #  elif (alarmlim_list[i]['unit']=="DoF" or alarmlim_list[i]['unit']=="DoC"):
                #        alarmlim_list[i]['unit']="DoC"
                #        rsp=get_centigrade(rsp,1)
            else:
                  if alarmlim_list[i]['unit']=="oC":
                        alarmlim_list[i]['unit']="oF"
                #  elif alarmlim_list[i]['unit']=="DoC":
                #        alarmlim_list[i]['unit']="DoF"
            
            alarmlim_list[i]['value']="{:.1f}".format(rsp)
   
