import paho.mqtt.client as mqtt
import json
import db_class

class MyMQTTClass(mqtt.Client):
    '''
    def __init__(self):
        self.jsonData = ""
        self.topic = ""
        self.dev_name = ""
        self.sensor_name = ""
        self.interface = ""
        self.sensor_type = ""
        self.data_type = ""
        self.delay_time = ""
        self.valid_max = ""
        self.valid_min = ""
    '''    
    def on_connect(self, mqttc, obj, flags, rc):
        print("rc : " +str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
        print("test : " + msg.topic)
        
    def on_publish(self, mqttc, obj, msg):
        print("mid : "+str(mid))

    def on_subscribe(self, mqttc, obj, mid, granted_qos):
        print("Subscribed : "+str(mid)+" "+str(granted_qos))

    def on_log(self, mqttc, obj, level, string):
        print(string)

    def on_message_value(self, mqttc, obj, msg):
        #if valid -> insert
        recvData = str(msg.payload.decode("utf-8"))
        self.jsonData = json.loads(recvData)
        temperature = str(self.jsonData["sensor_value"]["value"])
        time = str(self.jsonData["sensor_value"]["time"])
        print(temperature + time)
        #if(msg.topic == )

    def on_message_meta(self, mqttc, obj, msg):
        print("meta : "+ msg.topic + str(msg.payload))
        #self.db = DB()
        self.metaData = json.loads(str(msg.payload.decode("utf-8")))
        self.meta_topic = str(self.metaData["meta_info"]["topic"])
        tup = db.selectSensorINFO(self.meta_topic)
        #tup = db.selectSensorINFO('reading/temperature/test1')
            
        print(tup)

    def run(self):
        self.connect("127.0.0.1", 1883)
        self.subscribe("jsontopic")
        self.subscribe("reading/temperature/test1")
        self.message_callback_add("reading/temperature/test1", self.on_message_value)
        self.message_callback_add("jsontopic", self.on_message_meta)
        rc = 0
        while rc == 0:
            rc = self.loop()
        return rc

mqttc = MyMQTTClass()
db = db_class.DB()
rc = mqttc.run()

print("rc: "+str(rc))
        

