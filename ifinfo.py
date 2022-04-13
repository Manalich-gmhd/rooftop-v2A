#!/usr/bin/python3
#
# Using the 'netifaces' module to get interface data
# for IPV4
#
import netifaces
from netifaces import AF_INET
import ast


class Ife:

    def __init__(self):

        self.present = False
        self.address = '0.0.0.0'
        self.netmask = '0.0.0.0'
        self.broadcast = '0.0.0.0'
        self.gateway = '0.0.0.0'

# Class for each interface.
eth0 = Ife()
wlan0 = Ife()

# Interfaces: ['lo', 'eth0', 'wlan0', 'eth0:bas']
ifeList = netifaces.interfaces()

# If 'eth0' is present.
if 'eth0' in ifeList:
    try:
        # ifaddresses() returns: [{'addr': '127.0.0.1', 'netmask': '255.0.0.0', 'peer': '127.0.0.1'}]
        addresses = netifaces.ifaddresses('eth0')[AF_INET]
        address = ast.literal_eval(str(addresses))[0]
        # Set flag.
        eth0.present = True
        # Get data.
        eth0.address = address['addr']
        eth0.netmask = address['netmask']
        eth0.broadcast = address['broadcast']
    except KeyError:
        pass

# If 'wlan0' is present.
if 'wlan0' in ifeList:
    try:
        # ifaddresses() returns: [{'addr': '127.0.0.1', 'netmask': '255.0.0.0', 'peer': '127.0.0.1'}]
        addresses = netifaces.ifaddresses('wlan0')[AF_INET]
        address = ast.literal_eval(str(addresses))[0]
        # Set flag.
        wlan0.present = True
        # Get data.
        wlan0.address = address['addr']
        wlan0.netmask = address['netmask']
        wlan0.broadcast = address['broadcast']
    except KeyError:
        pass

# Get gateways for AF_INET.
# Returns array of tuples: [('192.168.1.254', 'eth0', True)]
try:
    gateways = netifaces.gateways()[AF_INET]
    gateways = ast.literal_eval(str(gateways))
    # For each tuple.
    for gateway in gateways:
        if gateway[1] == 'eth0':
            eth0.gateway = gateway[0]
        elif gateway[1] == 'wlan0':
            wlan0.gateway = gateway[0]
except KeyError:
    pass

#
# Output data in xml format.
#

print('<ifinfo>')
print('    <ife>')
print('        <name>eth0</name>')
print('        <address>'   + eth0.address   + '</address>')
print('        <netmask>'   + eth0.netmask   + '</netmask>')
print('        <broadcast>' + eth0.broadcast + '</broadcast>')
print('        <gateway>'   + eth0.gateway   + '</gateway>')
print('    </ife>')
print('    <ife>')
print('        <name>wlan0</name>')
print('        <address>'   + wlan0.address   + '</address>')
print('        <netmask>'   + wlan0.netmask   + '</netmask>')
print('        <broadcast>' + wlan0.broadcast + '</broadcast>')
print('        <gateway>'   + wlan0.gateway   + '</gateway>')
print('    </ife>')
print('</ifinfo>')

# And return.
exit(0)
