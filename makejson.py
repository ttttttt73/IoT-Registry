import json
from collections import OrderedDict
import tkinter as tk
from tkinter import filedialog

json_data = ""


# Ready for data
def sensor_json():
    group_data = OrderedDict()
    meta_info = OrderedDict()
    valid = OrderedDict()

    group_data["type"] = "Sensor"
    group_data["ID"] = "004s"

    meta_info["topic"] = "reading/mpu6050"
    meta_info["dev_name"] = "rpi"
    meta_info["sensor_name"] = "mpu6050"
    meta_info["interface"] = "I2C"
    meta_info["sensor_type"] = "Angular velocity"
    meta_info["data_type"] = "float"
    meta_info["delay_time"] = "600"
    meta_info["value_type"] = ['x', 'y', 'z']
    # valid["value"] = None

    valid["x_max"] = "100"
    valid["x_min"] = "0"
    valid["y_max"] = "100"
    valid["y_min"] = "0"
    valid["z_max"] = "100"
    valid["z_min"] = "0"

    meta_info["valid"] = valid
    group_data["meta_info"] = meta_info

    sensor_meta = json.dumps(group_data, ensure_ascii=False, indent="\t")

    # Write JSON

    with open('mpu6050.json', 'w', encoding="utf-8") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")

    return sensor_meta

def actuaotr_json():
    group_data = OrderedDict()
    meta_info = OrderedDict()
    command = OrderedDict()

    group_data["type"] = "Actuator"
    group_data["ID"] = "004s"

    meta_info["topic"] = "reading/mpu6050"
    meta_info["dev_name"] = "rpi"
    meta_info["sensor_name"] = "mpu6050"
    meta_info["interface"] = "I2C"
    meta_info["sensor_type"] = "Angular velocity"
    meta_info["data_type"] = "float"
    meta_info["delay_time"] = "600"
    meta_info["value_type"] = ['x', 'y', 'z']
    meta_info["commnad"] = ['on', 'off']
    # valid["value"] = None

    command["x_max"] = "100"
    command["x_min"] = "0"
    command["y_max"] = "100"
    command["y_min"] = "0"
    command["z_max"] = "100"
    command["z_min"] = "0"

    meta_info["valid"] = command
    group_data["meta_info"] = meta_info

    actuator_meta = json.dumps(group_data, ensure_ascii=False, indent="\t")

    # Write JSON

    with open('mpu6050.json', 'w', encoding="utf-8") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")

    return actuator_meta


def loadjson():
    global json_data
    root = tk.Tk()
    root.withdraw()
    json_path = filedialog.askopenfilename()
    if len(json_path) > 0:
        with open(json_path) as json_file:
            json_data = json.load(json_file)
            json_data = json.dumps(json_data, indent=4, sort_keys=True)


if __name__ == "__main__":
    # sensor_meta = makejson()
    actuaotr_json()
    loadjson()
    print("json : ", json_data)
