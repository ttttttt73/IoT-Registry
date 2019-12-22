import paho.mqtt.client as mqtt
import time
import Adafruit_HTU21D.HTU21D as HTU21D
from xml.etree.ElementTree import Element, dump, ElementTree, SubElement, parse, tostring
import time
from sys import argv
import datetime
import RPi.GPIO as GPIO
import xml.etree.ElementTree as ET
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from lxml import etree

cred = credentials.Certificate("./rpitt-34560-firebase-adminsdk-4gx7p-dba57e6a4f.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def on_weather():
   sensor = HTU21D.HTU21D()
   return  sensor

def on_publish():
   broker_address = "127.0.0.1"
   broker_portno = 1883
   client = mqtt.Client()

   client.connect(broker_address, broker_portno)

   s = on_weather()
   
   print ('Temp = {0:0.2f} *C'.format(s.read_temperature()))
   print ('Humidity  = {0:0.2f} %'.format(s.read_humidity()))
   print ('Dew Point = {0:0.2f} *C'.format(s.read_dewpoint()))

   unix = int(time.time())
   date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
   timing = str(datetime.datetime.fromtimestamp(unix).strftime('%H:%M:%S'))

#xml writing
   root = Element("devlist")

   node1 = Element("dev", name="Arduino")
   root.append(node1)

#arduino
   node1sub1 = SubElement(node1, "value", name="Smoke")
   node1sub1.text = "100"

   node1sub2 = SubElement(node1, "time")
   node1sub2.text = date + " " + timing

#rpi
   node2 = Element("dev", name="RPi")
   root.append(node2)

   node2sub1 = SubElement(node2, "value", name="Temperature")
   node2sub1.text = '{0:0.2f} *C'.format(s.read_temperature())

   node2sub2 = SubElement(node2, "value", name="Humidity")
   node2sub2.text = '{0:0.2f} %'.format(s.read_humidity())

   node2sub2 = SubElement(node2, "time")
   node2sub2.text = date + " " + timing

   indent(root)
   #dump(root)

   #tt = str(ET.tostring(root, encoding="utf-8"))
   tt = ET.tostring(root, encoding="utf-8")
   tt1 = tt.decode(encoding='utf-8')
   print(tt1)
   ElementTree(root).write("note.xml", "utf-8")

#dtd validation
   dtd = etree.DTD('devdev.dtd')
   tree = etree.parse('note.xml')
   print(dtd.validate(tree))
   print(dtd.error_log.filter_from_errors())

   
#db insert
   new_dev_ref = db.collection(u'HomeAutomatic').document()
   new_dev_ref.set({
           u'time' : date + ' ' + timing,
           u'Temperature' : '{0:0.2f} *C'.format(s.read_temperature()),
           u'Humidity' : '{0:0.2f} %'.format(s.read_humidity())
   })
   try:
        doc = new_dev_ref.get()
        print(u'Document data: {}'.format(doc.to_dict()))
   except google.cloud.exceptions.NotFound:
        print(u'No such doucment!')
        
#mqtt publish
   client.publish(topic = "test", payload = tt1)

   time.sleep(1)



def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

if __name__ == "__main__":
  while True:
    on_publish()
