import paho.mqtt.publish as publish


def pubmultiple():
    msgs = [{'topic': "reading/temperature/test1", 'payload': "multiple 1"}, {'topic': "reading/temperature/test1", 'payload': "multiple 2"}]
    publish.multiple(msgs, hostname="127.0.0.1")


if __name__=="__main__":
    pubmultiple()
