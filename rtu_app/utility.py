import xml.etree.ElementTree as et
#import httpx
#import asyncio
#import json
import requests
import time
import socket


#IP_Controller="192.168.1.33"
IP_Controller="0.0.0.0"
"""
async def get_var_rtd(sIpAddress,iIndex):
   url='http://' + sIpAddress + '/cgi-bin/xml-cgi'
   data='<rdom fcn="get" doc="rtd" path="obj[' + str(iIndex) + ']/val_scl"/>'
   try:
      async with httpx.AsyncClient() as client:
         r = await client.post(url, data=data)
   except:
      return None
   return r
async def get_var_webv(sIpAddress,iIndex):
   url='http://' + sIpAddress + '/cgi-bin/xml-cgi'
   data='<rdom fcn="get" doc="webv" path="c[' + str(iIndex) + ']/val"/>'
   try:
      async with httpx.AsyncClient() as client:
         r = await client.post(url, data=data)
   except:
      return None
   return r

def get_value(sIpAddress,iIndex,type=0):
   if type==0:
      rsp=asyncio.run(get_var_rtd(sIpAddress,iIndex))
   else:
      rsp=asyncio.run(get_var_webv(sIpAddress,iIndex))
   if rsp.status_code !=200:
      return None   
   try:      
    value = float(et.fromstring(rsp.text).text)
   except:
    value = None
   return value
"""


   
def get_var_rtd_syn(iIndex):
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="get" doc="rtd" path="obj[' + str(iIndex) + ']/val_scl"/>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
   except:
      return None
   return rsp

def get_var_webv_syn(iIndex):
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="get" doc="webv" path="c[' + str(iIndex) + ']/val"/>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
   except:
      return None
   return rsp

def get_value_syn(iIndex,type=0):
   if type==0:
      rsp=get_var_rtd_syn(iIndex)
   else:
      rsp=get_var_webv_syn(iIndex)
   if rsp is not None:   
      if rsp.status_code != 200:
         return None
   else:
      return None 
   try:      
    value = float(et.fromstring(rsp.text).text)
   except:
    value = None
   return value

def get_evaluation():
   rsp=get_var_rtd_syn(83)
   if rsp is not None:
     if rsp.status_code !=200:
       return 0   
   try:      
    value = float(et.fromstring(rsp.text).text)
   except:
    value = 0
   return value

def get_compresors():
   rsp=get_var_rtd_syn(119)
   if rsp is not None:
      if rsp.status_code !=200:
         return 2   
   try:      
    value = float(et.fromstring(rsp.text).text)
   except:
    value = 2
   return value

def get_emergency():
   rsp=get_var_rtd_syn(23)
   if rsp is not None:
      if rsp.status_code !=200:
         return 0   
   try:      
    value = float(et.fromstring(rsp.text).text)
   except:
    value = 0
   return value
 
def get_value_stri(iIndex):
   rsp=get_var_rtd_syn(iIndex)
   if rsp is not None:
     if rsp.status_code !=200:
       return None   
   try:      
    value = str(int(float(et.fromstring(rsp.text).text)))
   except:
    value = None
   return value

def set_var_rtd(iIndex,vValue):
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="get" doc="rtd" path="obj[' + str(iIndex) + ']/ws_control"/>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
        # Parse XML.
        root = et.fromstring(rsp.text)
        # If request was ACK'd.
        if root.attrib['rsp'] == 'ack':
        # If point is under wire sheet control.
            if root.text == '1':
            # We can't write.
              return -1
            # Else we were NAK'd; SERIOUS PROBLEM
        else:
          return -1
        req = '<rdom fcn="set" doc="rtd" path="obj[' + str(iIndex) + ']/val_scl">' + str(vValue) + '</rdom>'
        # Try to execute POST request.
        try:
            # Execute POST and get response.
            rsp = requests.post(url, data=req , timeout=2)
            # If good HTML response.
            if (rsp.status_code == 200):
                # Parse XML.
                root = et.fromstring(rsp.text)
                #######################################################
                # This is the only place we can return success.
                #######################################################
                if root.attrib['rsp'] == 'ack':
                    return 0
            else:
                # Something there, but not BASpi.
                return -1
        except OSError:
            # Timeout.
            return -1
     else:
      return -1
   except OSError:
      return -1
   return -1    
   

def set_var_webv(iIndex,vValue):
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   #req='<rdom fcn="get" doc="webv" path="c[' + str(iIndex) + ']/ctl"/>'
   req='<rdom fcn="set" doc="webc.xml" path="c[' + str(iIndex) + ']">'+ str(vValue) + '</rdom>'
   
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
        # Parse XML.
        #root = et.fromstring(rsp.text)
        # If request was ACK'd.
        #if root.attrib['rsp'] == 'ack':
        # If point is under wire sheet control.
        #    if root.text == '1':
        #    # We can't write.
        #      return -1
            # Else we were NAK'd; SERIOUS PROBLEM
        #else:
        #  return -1
        req='<rdom fcn="set" doc="webv" path="c[' + str(iIndex) + ']/val">'+ str(vValue) + '</rdom>'
        try:
            # Execute POST and get response.
            rsp = requests.post(url, data=req , timeout=2)
            # If good HTML response.
            if (rsp.status_code == 200):
                # Parse XML.
                root = et.fromstring(rsp.text)
                #######################################################
                # This is the only place we can return success.
                #######################################################
                if root.attrib['rsp'] == 'ack':
                    return 0
            else:
                # Something there, but not BASpi.
                return -1
        except OSError:
            # Timeout.
            return -1
     else:
         return -1     
   except OSError:
      return -1
   return -1

def set_value(iIndex,vValue,type=0):
   if type==0:
      rsp=set_var_rtd(iIndex,vValue)
   else:
      rsp=set_var_webv(iIndex,vValue)
   return rsp

def reset_energy():
   rsp=set_var_webv(33,1)
   #wait three seconds
   time.sleep(3)
   rsp=set_var_webv(33,0)
   return rsp

def open_write_webv():
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="mode" doc="webc.xml" mode="W"/>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
       return 0
   except OSError:
      return -1
    
    
def save_webv():
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="set" doc="sys" path="save_xml">webc.xml</rdom>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
       return 0
   except OSError:
      return -1
    
def open_read_webv():
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="mode" doc="webc.xml" mode="R"/>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
       return 0
   except OSError:
      return -1
  
def open_write_virtual():
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="mode" doc="bas_cfg.xml" mode="W"/>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
       return 0
   except OSError:
      return -1
    
    
def set_initial_virtual(iIndex,vValue):
   ix=iIndex-38
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="set" doc="bas_cfg.xml" path="unit_cfg[1]/chn_cfg[' + str(ix) + ']/initial_val">'+ str(vValue) +'</rdom>'
   
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
        # Parse XML.
        root = et.fromstring(rsp.text)
        # If request was ACK'd.
        if root.attrib['rsp'] == 'ack':
          return 0
        else:
          return -1
     else:
         return -1     
   except OSError:
      return -1
   return -1
    


def save_virtual():
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="set" doc="sys" path="save_xml">bas_cfg.xml</rdom>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
       return 0
   except OSError:
      return -1

# 4th <rdom fcn="set" doc="sys" path="chn_data">41</rdom>


def open_read_virtual():
   url='http://' + IP_Controller + '/cgi-bin/xml-cgi'
   req='<rdom fcn="mode" doc="bas_cfg.xml" mode="R"/>'
   try:
     rsp = requests.post(url, data=req , timeout=2)
     if (rsp.status_code == 200):
       return 0
   except OSError:
      return -1


def get_ip():
    """Pirated from the interweb"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip
 
def get_centigrade(vValue,delta=0):
    if delta==0:
     convertion=(vValue - 32) * 0.5556
    else:
      convertion=vValue * 0.5556
    return convertion
 
def get_fahrenheit(vValue):
     return vValue*1.8+32
