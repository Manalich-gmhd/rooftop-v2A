from rtu_app.utility import get_value_syn,get_centigrade

def init_alarm_vars(alarm_list):
      var = {}
      var['name']='High Coil Temp.'
      var['index']=63
      var['value']="0"
      var['limit_index']=127
      var['limit_value']="0.0"
      var['limit_unit']="oF"
      alarm_list.append(var)
      var = {}
      var['name']='Low Suct. Press. C1'
      var['index']=58
      var['value']="0"
      var['limit_index']=123
      var['limit_value']="0.0"
      var['limit_unit']="psi"
      alarm_list.append(var)
      var = {}
      var['name']='High Suct. Press. C1'
      var['index']=57
      var['value']="0"
      var['limit_index']=124
      var['limit_value']="0.0"
      var['limit_unit']="psi"
      alarm_list.append(var)
      var = {}
      var['name']='Low Superheat C1'
      var['index']=52
      var['value']="0"
      var['limit_index']=125
      var['limit_value']="0.0"
      var['limit_unit']="DoF"
      alarm_list.append(var)
      var = {}
      var['name']='High Superheat C1'
      var['index']=50
      var['value']="0"
      var['limit_index']=126
      var['limit_value']="0.0"
      var['limit_unit']="DoF"
      alarm_list.append(var)

      var = {}
      var['name']='Low Suct. Press. C2'
      var['index']=62
      var['value']="0"
      var['limit_index']=123
      var['limit_value']="0.0"
      var['limit_unit']="psi"
      alarm_list.append(var)
      var = {}
      var['name']='High Suct. Press. C2'
      var['index']=61
      var['value']="0"
      var['limit_index']=124
      var['limit_value']="0.0"
      var['limit_unit']="psi"
      alarm_list.append(var)
      var = {}
      var['name']='Low Superheat C2'
      var['index']=60
      var['value']="0"
      var['limit_index']=125
      var['limit_value']="0.0"
      var['limit_unit']="DoF"
      alarm_list.append(var)
      var = {}
      var['name']='High Superheat C2'
      var['index']=59
      var['value']="0"
      var['limit_index']=126
      var['limit_value']="0.0"
      var['limit_unit']="DoF"
      alarm_list.append(var)
      var = {}
      var['name']='Low Press. Prot. C1'
      var['index']=179
      var['value']="0"
      var['limit_index']=109
      var['limit_value']="0.0"
      var['limit_unit']="psi"
      alarm_list.append(var)
      var = {}
      var['name']='Low Press. Prot. C2'
      var['index']=180
      var['value']="0"
      var['limit_index']=109
      var['limit_value']="0.0"
      var['limit_unit']="psi"
      alarm_list.append(var)
      var = {}
      var['name']='Fail Fan Prot.'
      var['index']=181
      var['value']="0"
      var['limit_index']=182
      var['limit_value']="0.0"
      var['limit_unit']="kW"
      alarm_list.append(var)
      var = {}
      var['name']='VSD Alarm'
      var['index']=186
      var['value']="0"
      var['limit_index']=-1
      var['limit_value']=""
      var['limit_unit']=""
      alarm_list.append(var)

def update_alarm(alarm_list, all=True,conv=0):
   for i in range(len(alarm_list)):
      rsp=get_value_syn(alarm_list[i]['index'])
      if rsp is not None:
         if rsp>0:
            alarm_list[i]['value']="Active"
         else:
            alarm_list[i]['value']="Inactive"
      if all and alarm_list[i]['limit_index']>=0:             
        rsp=get_value_syn(alarm_list[i]['limit_index'])
        if rsp is not None:
           
            if conv>0:
               if (alarm_list[i]['limit_unit']=="oF" or alarm_list[i]['limit_unit']=="oC"):
                 alarm_list[i]['limit_unit']="oC"
                 rsp=get_centigrade(rsp)
            #   elif (alarm_list[i]['limit_unit']=="DoF" or alarm_list[i]['limit_unit']=="DoC"):
            #      alarm_list[i]['limit_unit']="DoC"
            #      rsp=get_centigrade(rsp,1)
            else:
               if alarm_list[i]['limit_unit']=="oC":
                  alarm_list[i]['limit_unit']="oF"
            #   elif alarm_list[i]['limit_unit']=="DoC":
            #      alarm_list[i]['limit_unit']="DoF"

            alarm_list[i]['limit_value']="{:.1f}".format(rsp)
   
