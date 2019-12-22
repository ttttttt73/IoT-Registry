import paho.mqtt.client as mqtt
import time
import Adafruit_HTU21D.HTU21D as HTU21D
import time
from sys import argv
import datetime
import json
from collections import OrderedDict

#  SCL = P9_19 and SDA = P9_20
def on_weather():
   sensor = HTU21D.HTU21D()
   return  sensor

def on_publish():
   broker_address = "127.0.0.1"
   broker_portno = 1883
   client = mqtt.Client()

   client.connect(broker_address, broker_portno)
   
   #make json (metadata)
   group_data = OrderedDict()
   meta_info = OrderedDict()
    
   meta_info["topic"] = "reading/temperature/test1"
   meta_info["dev_name"] = "rpi"
   meta_info["sensor_name"] = "HTU21D"
   meta_info["interface"] = "I2C"
   meta_info["sensor_type"] = "temperature"
   meta_info["data_type"] = "float"
   meta_info["delay_time"] = "600"
   meta_info["valid_max"] = "50"
   meta_info["valid_min"] = "-30"

 
   group_data["meta_info"] = meta_info
 
   sensor_meta = json.dumps(group_data, ensure_ascii=False, indent="\t")
 
   print(sensor_meta)
 
   #sensing the value
   s = on_weather()
   #tmp = -200
   tmp = '{0:0.2f}'.format(s.read_temperature())
   print(tmp) 
   unix = int(time.time())
   date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
   timing = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))
   tstamp = str(datetime.datetime.fromtimestamp(unix))

   #make json(sensing value)
   group_data2 = OrderedDict()
   sensor_value = OrderedDict()
   sensor_value["value"] = tmp
   sensor_value["time"] = tstamp
   group_data2["sensor_value"] = sensor_value

   sensor_data = json.dumps(group_data2, ensure_ascii=False, indent="\t")
   print(sensor_data)
  
   client.publish(topic = "jsontopic", payload = sensor_meta)
   client.publish(topic = "reading/temperature/test1", payload = sensor_data)
   time.sleep(1)

if __name__ == "__main__":
   on_publish()
