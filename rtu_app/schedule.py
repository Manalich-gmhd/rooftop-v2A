from rtu_app.utility import get_value_syn,get_value_stri

def init_schedule_vars(schedule_list):
      var = {}
      var['name']='Weekdays'
      var['index_hon']=89
      var['index_mon']=90
      var['index_hoff']=91
      var['index_moff']=92
      var['value_on']="00:00"
      var['value_off']="00:00"
      schedule_list.append(var)
      var = {}
      var['name']='Saturday'
      var['index_hon']=97
      var['index_mon']=98
      var['index_hoff']=99
      var['index_moff']=100
      var['value_on']="00:00"
      var['value_off']="00:00"
      schedule_list.append(var)
      var = {}
      var['name']='Sunday'
      var['index_hon']=93
      var['index_mon']=94
      var['index_hoff']=95
      var['index_moff']=96
      var['value_on']="00:00"
      var['value_off']="00:00"
      schedule_list.append(var)
      
def update_schedule(schedule_list):
   for i in range(len(schedule_list)):
      h_on=get_value_stri(schedule_list[i]['index_hon'])
      m_on=get_value_stri(schedule_list[i]['index_mon'])
      h_off=get_value_stri(schedule_list[i]['index_hoff'])
      m_off=get_value_stri(schedule_list[i]['index_moff'])
      try:
            schedule_list[i]['value_on']=h_on.zfill(2)+':'+m_on.zfill(2)
            schedule_list[i]['value_off']=h_off.zfill(2)+':'+m_off.zfill(2)
      except:
            error=True      

def get_schedule_enable():  
    rsp=get_value_syn(87)
    if rsp is not None:
      return int(rsp)
    else:
          return 0