import json
from collections import OrderedDict
import tkinter as tk
from tkinter import filedialog

json_data = ""

# Ready for data
def metainfo_json():
    group_data = OrderedDict()
    meta_info = OrderedDict()
    valid = OrderedDict()

    group_data["type"] = "Sensor"
    group_data["topic"] = "reading/htu21d"
    group_data["dev_name"] = "rpi"
    group_data["sensor_name"] = "htu21d"
    group_data["interface"] = "I2C"
    group_data["sensor_type"] = "Temperature"
    group_data["data_type"] = "float"
    group_data["delay_time"] = "600"
    group_data["value_type"] = "temperature"
    # group_data["commnad"] = ['on', 'off']
    group_data["commnad"] =  None

    """valid["x_max"] = "100"
    valid["x_min"] = "0"
    valid["y_max"] = "100"
    valid["y_min"] = "0"
    valid["z_max"] = "100"
    valid["z_min"] = "0"""

    valid["max"] = 100
    valid["min"] = -20

    group_data["valid"] = valid

    sensor_meta = json.dumps(group_data, ensure_ascii=False, indent="\t")

    # Write JSON
    with open('htu21d.json', 'w', encoding="utf-8") as make_file:
        json.dump(group_data, make_file, ensure_ascii=False, indent="\t")

    return sensor_meta


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
    metainfo_json()
    loadjson()
    print("json : ", json_data)
    # rint(metainfo_json())
