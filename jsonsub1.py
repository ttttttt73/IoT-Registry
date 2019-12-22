import paho.mqtt.client as mqtt
import json
import MySQLdb

recvData = ""
topic = ""
dev_name = ""
sensor_name = ""
interface = ""
sensor_type = ""
data_type = ""
delay_time = ""
valid_max = ""
valid_min = ""


# db insert
def dev_writesql():
    c = ""
    conn = ""
    try:
        conn = MySQLdb.connect("localhost", "pi", "pi", "dev_regi")
        c = conn.cursor()
        global dev_name
        global sensor_name
        global interface
        global sensor_type
        global data_type
        global delay_time
        global valid_max
        global valid_min
        query = "SELECT topic FROM SensorINFO WHERE topic = '" + topic + "'"
        c.execute(query)
        search = c.fetchone()
        print(search)
        print(search[0])
        if (search == None):
            print('Inseting MetaINFO...')
            sql = "INSERT INTO SensorINFO (topic, dev_name, sensor_name, interface, sensor_type, data_type, delay_time, valid_max, valid_min) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            c.execute(sql, (
            topic, dev_name, sensor_name, interface, sensor_type, data_type, delay_time, valid_max, valid_min))
            conn.commit()
    except Exception as e:
        print("Got exception " + str(e))
    finally:
        c.close()
        conn.close()


# the callback function
def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code {}".format(rc))
    # client.subscribe("sensor/temperature")
    client.subscribe("jsontopic")
    client.subscribe("reading/temperature/test1")


def on_disconnect(client, userdata, rc):
    print("Disconnected From Broker")


def on_message(client, userdata, message):
    # print(message.payload.decode("utf-8"))
    print(message.topic)
    recvData = str(message.payload.decode("utf-8"))
    print("received message = ", recvData)
    jsonData = json.loads(recvData)
    # print("Topic : " + str(jsonData["meta_info"]["topic"]))
    global topic
    global dev_name
    global sensor_name
    global interface
    global sensor_type
    global data_type
    global delay_time
    global valid_max
    global valid_min
    topic = str(jsonData["meta_info"]["topic"])
    dev_name = str(jsonData["meta_info"]["dev_name"])
    sensor_name = str(jsonData["meta_info"]["sensor_name"])
    interface = str(jsonData["meta_info"]["interface"])
    sensor_type = str(jsonData["meta_info"]["sensor_type"])
    data_type = str(jsonData["meta_info"]["data_type"])
    delay_time = str(jsonData["meta_info"]["delay_time"])
    valid_max = str(jsonData["meta_info"]["valid_max"])
    valid_min = str(jsonData["meta_info"]["valid_min"])
    dev_writesql()


def on_message_value(client, userdata, message):
    recvData = str(message.payload.decode("utf-8"))
    jsonData = json.loads(recvData)
    temperature = str(jsonData["sensor_value"]["temperature"])
    time = str(jsonData["sensor_value"]["time"])
    global topic
    try:
        conn = MySQLdb.connect("localhost", "pi", "pi", "dev_regi")
        c = conn.cursor()
        # squery1 = "SELECT "
        vquery1 = "SELECT valid_max FROM SensorINFO WHERE topic = '" + message.topic + "'"
        vquery2 = "SELECT valid_min FROM SensorINFO WHERE topic = '" + message.topic + "'"
        c.execute(vquery1)
        valid_max = c.fetchone()
        print("valid_max : " + valid_max[0])
        c.execute(vquery2)
        valid_min = c.fetchone()
        print("valid_min : " + valid_min[0])
        if (valid_max[0] != None and valid_max[0] != None):
            if (float(temperature) <= float(valid_max[0]) and float(temperature) >= float(valid_min[0])):
                print("value Inserting...")
                query = "INSERT INTO Reading (topic, value, time) VALUES (%s, %s, %s)"
                c.execute(query, (topic, temperature, time))
            else:
                print("Value is invalid!")
        conn.commit()
    except Exception as e:
        print("Got exception : " + str(e))
    finally:
        c.close()
        conn.close()
        '''def search_db():
        #query = "SELECT * FROM Reading"
        pass 
        def insert_db():
        query = "INSERT INTO Reading (topic, value, time) VALUES (%s, %s, %s)"
        c.execute(query, (temperature, time)) 
        pass'''
    print("value load")
    print(message.topic)
    print(message.payload.decode("utf-8"))


broker_address = "127.0.0.1"
broker_portno = 1883
client = mqtt.Client()

# Assigning the object attribute to the Callback Function
client.message_callback_add("reading/temperature/test1", on_message_value)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect(broker_address, broker_portno)

client.loop_forever()
