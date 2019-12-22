import paho.mqtt.client as mqtt
from queue import Queue
import logging
logger = logging.getLogger(__name__)

class MqttClient(mqtt.Client)
    def __init__(self):
        self._queue = Queue()
        self.connected = False
        super().__init__(client_id=client_id, clean_session=clean_session, userdata=userdata,  protocol=protocol, transport=transport)

    def configure(self, hostname, port, timeout=60, sslcontext=None):
        self.hostnmae = hostname
        self.port = port
        self.timeout = timeout
        self.sslcontext = sslcontext

