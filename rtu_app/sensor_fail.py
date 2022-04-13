from rtu_app.utility import get_value_syn,get_centigrade

def init_fail_vars(fail_list):
      var = {}
      var['name']='Coil Temperature Fail'
      var['index']=135
      var['value']="0"
      var['limit_lo_index']=115
      var['limit_lo_value']="0.0"
      var['limit_lo_index_ON']=117
      var['limit_lo_value_ON']="0.0"
      var['limit_hi_index']=116
      var['limit_hi_value']="0.0"
      var['limit_hi_index_ON']=118
      var['limit_hi_value_ON']="0.0"
      var['limit_unit']="oF"
      fail_list.append(var)
      var = {}
      var['name']='Suct. Temp. C1 Fail'
      var['index']=133
      var['value']="0"
      var['limit_lo_index']=111
      var['limit_lo_value']="0.0"
      var['limit_lo_index_ON']=113
      var['limit_lo_value_ON']="0.0"
      var['limit_hi_index']=112
      var['limit_hi_value']="0.0"
      var['limit_hi_index_ON']=114
      var['limit_hi_value_ON']="0.0"
      var['limit_unit']="oF"
      fail_list.append(var)
      var = {}
      var['name']='Suct. Press. C1 Fail'
      var['index']=131
      var['value']="0"
      var['limit_lo_index']=107
      var['limit_lo_value']="0.0"
      var['limit_lo_index_ON']=109
      var['limit_lo_value_ON']="0.0"
      var['limit_hi_index']=108
      var['limit_hi_value']="0.0"
      var['limit_hi_index_ON']=110
      var['limit_hi_value_ON']="0.0"
      var['limit_unit']="psi"
      fail_list.append(var)
      var = {}
      var['name']='Suct. Temp. C2 Fail'
      var['index']=134
      var['value']="0"
      var['limit_lo_index']=111
      var['limit_lo_value']="0.0"
      var['limit_lo_index_ON']=113
      var['limit_lo_value_ON']="0.0"
      var['limit_hi_index']=112
      var['limit_hi_value']="0.0"
      var['limit_hi_index_ON']=114
      var['limit_hi_value_ON']="0.0"
      var['limit_unit']="oF"
      fail_list.append(var)
      var = {}
      var['name']='Suct. Press. C2 Fail'
      var['index']=132
      var['value']="0"
      var['limit_lo_index']=107
      var['limit_lo_value']="0.0"
      var['limit_lo_index_ON']=109
      var['limit_lo_value_ON']="0.0"
      var['limit_hi_index']=108
      var['limit_hi_value']="0.0"
      var['limit_hi_index_ON']=110
      var['limit_hi_value_ON']="0.0"
      var['limit_unit']="psi"
      fail_list.append(var)
      
def update_fail(fail_list, all=True,conv=0):
   for i in range(len(fail_list)):
      rsp=get_value_syn(fail_list[i]['index'])
      if rsp is not None:
         if rsp>0:
            fail_list[i]['value']="Active"
         else:
            fail_list[i]['value']="Inactive"
      if all:   
        make_conv=False  
        if conv>0:
            if (fail_list[i]['limit_unit']=="oF" or fail_list[i]['limit_unit']=="oC"):
                fail_list[i]['limit_unit']="oC"
                make_conv=True  
        else:
            if fail_list[i]['limit_unit']=="oC":
                fail_list[i]['limit_unit']="oF"
          
        rsp=get_value_syn(fail_list[i]['limit_lo_index'])
        if rsp is not None:
            if make_conv>0:
                 rsp=get_centigrade(rsp)
            fail_list[i]['limit_lo_value']="{:.1f}".format(rsp)
        rsp=get_value_syn(fail_list[i]['limit_lo_index_ON'])
        if rsp is not None:
            if make_conv>0:
                 rsp=get_centigrade(rsp)
            fail_list[i]['limit_lo_value_ON']="{:.1f}".format(rsp)
        rsp=get_value_syn(fail_list[i]['limit_hi_index'])
        if rsp is not None:
            if make_conv>0:
                 rsp=get_centigrade(rsp)
            fail_list[i]['limit_hi_value']="{:.1f}".format(rsp)
        rsp=get_value_syn(fail_list[i]['limit_hi_index_ON'])
        if rsp is not None:
            if make_conv>0:
                 rsp=get_centigrade(rsp)
            fail_list[i]['limit_hi_value_ON']="{:.1f}".format(rsp)
      
