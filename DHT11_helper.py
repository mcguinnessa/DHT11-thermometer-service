
import Adafruit_DHT

DATA_PIN = 23

class dht11_helper:

   class DeviceException(Exception):
      pass

   class DeviceTimeoutException(Exception):
      pass

   ###############################################################
   # 
   #  Gets the raw data from the device file
   # 
   ###############################################################
   @staticmethod
   def read_data():

      # Try to grab a sensor reading.  Use the read_retry method which will retry up
      # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
      humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DATA_PIN)

      # Note that sometimes you won't get a reading and
      # the results will be null (because Linux can't
      # guarantee the timing of calls to read the sensor).
      # If this happens try again!
      if humidity is None or temp_c is None:
         raise dht11_helper.DeviceTimeoutException

      temp_f = temp_c * 9/5.0 + 32
      return temp_c, temp_f, humidity

