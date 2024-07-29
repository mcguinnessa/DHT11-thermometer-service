#!/usr/bin/python3

import sys, getopt

from DHT11_helper import dht11_helper
 
newline='\n'

try:
   opts, args = getopt.getopt(sys.argv[1:],"n",["nonewline"])
except getopt.GetoptError:
   print('<get_temp.py -n>')
   sys.exit(2)

for opt, arg in opts:
   if opt == '-h':
      print('<get_temp.py -n>')
      sys.exit()
   elif opt in ("-n", "--nonewline"):
     newline=''

dht11_helper.read_data = staticmethod(dht11_helper.read_data)

celcius,farenheit,humidity = dht11_helper.read_data()

print("%0.2f" % (humidity), end=newline)

