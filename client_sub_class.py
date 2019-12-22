# import context
import paho.mqtt.client as mqtt
import json
import tkinter as tk
from tkinter import filedialog
from queue import Queue
# import db_class
import makejson

class MyMQTTClass(mqtt.Client):
    def on_connect(self, mqttc, obj, flags, rc):
        print("rc : " +str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        self.topic = msg.topic
        
    def on_publish(self, mqttc, obj, msg):
        print("mid : "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed : "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def on_message(self, mqttc, obj, msg):
        self._queue.put(msg)

    def get_queue(self):
        return self._queue

    def on_message_value(self, mqttc, obj, msg):
        #if valid -> insert
        # recvData = str(message.payload.decode("utf-8"))
        # jsonData = json.loads(recvData)
        value = str(jsonData["sensor_value"]["temperature"])
        time = str(jsonData["sensor_value"]["time"])
        # if(message.topic == )

    def on_message_meta(self, mqttc, obj, msg):
        # self.metadata = str(message.payload.decode("utf_8"))
        # self.metajson = json.laods(recvdata)
        pass

    def load_json(self):
        self.root = tk.Tk()
        self.root.withdraw()
        json_path = filedialog.askopenfilename()

        with open(json_path) as json_file:
            json_data = json.load(json_file)
        print(json_data)
        return json_data

    def set_meta_configure(self):
        self.load_json()
        self.type = str(self.metajson["type"])
        self.id = str(self.metajson["ID"])
        self.topic = str(self.metajson["meta_info"]["topic"])
        self.dev_name = str(self.metajson["meta_info"]["dev_name"])
        self.sensor_name = str(self.metajson["meta_info"]["sensor_name"])
        self.interface = str(self.metajson["meta_info"]["interface"])
        self.sensor_type = str(self.metajson["meta_info"]["sensor_type"])
        self.data_type = str(self.metajson["meta_info"]["data_type"])
        self.delay_time = str(self.metajson["meta_info"]["delay_time"])
        self.valid = str(self.metajson["meta_info"]["valid"])

    '''def set_value_config(self):
        self.value = [""]["value"]
        self.time = [""]["time"]'''

    def set_configure(self, ip, topic):
        self.ip = ip
        self.topic = topic

    def run(self):
        self._queue = Queue()
        self.connected = False
        self.connect("127.0.0.1", 1883) # IP address
        # self.subscribe("jsontopic") # Topic name
        self.subscribe("reading/temperature/test1")
        # self.subscribe("reading/#")
        self.publish(topic="jsontopic", payload="publish_test")
        msgs = [{'topic': "paho/test/multiple", 'payload': "multiple 1"},
                ("paho/test/multiple", "multiple 2", 0, False)]
        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc

    def create(self):
        self.person = MyMQTTClass()

    def close(self):
        self.loop_stop()
        self.disconnect()


def setData():
    global topics, wildtopics
    topics = ()


if __name__ == "__main__":
    mqttc = MyMQTTClass()
    rc = mqttc.run()

    print("rc: "+str(rc))

# person = MyMQTTClass()

