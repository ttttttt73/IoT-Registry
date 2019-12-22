class Mqclient:
    def __init__(self, topic, dev_name, sensor_name, interface, sensor_type, data_type, delay_time):
        self.topic = topic
        self.dev_name = dev_name
        self.sensor_name = sensor_name
        self.interface = interface
        self.sensor_type = sensor_type
        self.data_type = data_type
        self.delay_time


    def insert(self):
        execute("INSET INTO SensorINFO (topic, dev_name,....)
    def isSQL(self):
        pass


def dev_writesql(topic, dev_name, sensor_name, interface, sensor_type, data_type, delay_time):
                try:
                
def jsonpar(stst):
            abc = str(jsonData["meta_info"][stst])
            return abc
            
def on_messasge(client, userdata, rc):
                recvData = str(message.payload.decode("utf-8"))
                print("received message = ", recvData)
                global jsonData
                jsonData = json.loads(recvData)

jsonData = ""
topic = ""          
r = sqlsql(~~~~~)
r.insert()
