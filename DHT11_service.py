from flask import Flask, jsonify

app = Flask(__name__)

from DHT11_helper import dht11_helper

C_INDEX = 0
F_INDEX = 1
H_INDEX = 2

######################################################################
#
# Get temperature and humidity with given index, format for errors
#
######################################################################
def get_sensor_data(idx):
   print("Received Call")

   try:
      rc =  {"value": dht11_helper.read_data()[idx]}
   except dht11_helper.DeviceException as e:
      print("Exception:" + str(e))
      rc = {"error:": "Device Not Found"}
#   except dht11_helper.DeviceFormatException as e:
#      print("Exception:" + str(e))
#      rc = {"error:": "Unexpected Format from device" }
   except dht11_helper.DeviceTimeoutException as e:
      print("Exception:" + str(e))
      rc = {"error:": "Timed out reading from device" }
   except Exception as e:
      print("Exception:" + str(e))
      rc = {"error:": "Unknown Exception" }

   print("T:" + str(rc))
   return jsonify(rc)


######################################################################
#
# Get temperature in Celcius
#
######################################################################
@app.route("/DHT11/c")
def celcius():
   return get_sensor_data(C_INDEX)
    
######################################################################
#
# Get temperature in Farenheit
#
######################################################################
@app.route("/DHT11/f")
def farenheit():
   return get_sensor_data(F_INDEX)
    
######################################################################
#
# Get temperature in Farenheit
#
######################################################################
@app.route("/DHT11/h")
def humidity():
   return get_sensor_data(H_INDEX)
    
