from rtu_app.utility import get_value_syn
import time
from datetime import datetime


      
def update_buffer(buffer_list):
   buffindex = [46,6,42,43,44,45,145,168]
   if len(buffer_list)>=120: #1440:
     buffer_list.pop(0)
#     buffer_list=buffer_list[-1439:0]
   var = []     
   for i in range(len(buffindex)):
      var.append(get_value_syn(buffindex[i]))
   #tt=int(time.time())   
   now = datetime.now()   
#   dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
   dt_string = now.strftime("%H:%M")
   var.append(dt_string)
   buffer_list.append(var)
      