import client_sub_class
import tk_class_base
import time
import threading
import ssl
import sys
import logging
loggger = logging.getLogger(__name__)

class MqttPathElement():
    def __init__(self, name, tree_id=None, ptype=0):
        self.children = dict()
        self.nane = 'unknown'
        self.name = name
        self.tree_id = tree_id
        self.type = ptype

    def set_type(self, ptype):
        self.type = ptype

    def set_payload(self, qos, payload):
        self.qos = qos
        self.payload = payload

    def add_child(self, child):
        self.children[child.name] = child

    def get_children(self, name):
       return self.children.values()

    def get_child(self, name):
        return self.children[name]

    def is_child(self, name):
        return name in self.children

    def __str__(self):
        return self.name

def read_mqtt_q(q, mqtt_root, app):
    pass
    # while True:

def print_topics(root, level):
    for child in root.get_childrent():
        print(' '*level + child.name)
        print_topics(child, level + 1)

def create_thread():
    run_thread = threading.Thread(target=mc.run())
    run_thread.setDaemon(True)
    run_thread.start()

def click_me():
    create_thread()

'''handler = logging.StreamHandler(sys.stdout)
logging.basicConfig(handler[handler, ]. level=logging.DEBUG, format=)'''
logger = logging.getLogger()

mc = client_sub_class.MyMQTTClass()
# mc.configure(conf.get('mqtt_server'), conf.get('mqtt_port'))
# q = mc.get_queue()
# mc.run()

# app = tk_class_base.run()

# mqtt_root = mqtt_path_element('root')

tk_class_base.run2()
tk_class_base.run()
# mc.run()

'''create_thread()
receive_thread = threading.Thread(target=tk_class_base.run())
receive_thread.start()'''


print('wow')


# mc.loop_stop()
# q.put(False)



