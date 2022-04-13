import requests
import time
IP_Controller="http://localhost:8060/save_historic"
#IP_Controller="http://0.0.0.0:8000/save_historic"

print("Start Program")  
while True:
  time.sleep(58)
  try:
    rsp = requests.get(IP_Controller)
  except:
    rs= "Err"
    print(rs)  
  

  
  
  