import json
from collections import OrderedDict


class regist:
    def __init__(self):
        pass

    def make_json(self):
        self.type = input('type을 입력해주세요(ex. Sensor, Actuator) :')
        print('type:', self.type)
        self.topic = input('topic을 입력해주세요 : ')
        print('topic:', self.topic)
        self.dev_name = input('dev_name을 입력해주세요 : ')
        print('dev_name:', self.dev_name)
        self.sensor_name = input('sensor_name을 입력해주세요 : ')
        print('sensor_name:', self.sensor_name)
        self.interface = input('interface을 입력해주세요 : ')
        print('interface:', self.interface)
        self.sensor_type = input('sensor_type을 입력해주세요 : ')
        print('sensor_type:', self.sensor_type)
        self.data_type = input('data_type을 입력해주세요 : ')
        print('data_type:', self.data_type)
        self.delay_time = input('delay_time을 입력해주세요 : ')
        print('delay_time:', self.delay_time)
        self.value_type = input('value_type을 입력해주세요(ex.temperature) : ')
        print('value_type:', self.value_type)
        self.command = input('command을 입력해주세요 : ')
        print('command:', self.command)
        self.valid_max = input('valid_max을 입력해주세요 : ')
        print('valid_max:', self.valid_max)
        self.valid_min = input('valid_min을 입력해주세요 : ')
        print('valid_min:', self.valid_min)

        self.group_data = OrderedDict()
        self.valid = OrderedDict()

        self.group_data["type"] = self.type
        self.group_data["topic"] = self.topic
        self.group_data["dev_name"] = self.dev_name
        self.group_data["sensor_name"] = self.sensor_name
        self.group_data["interface"] = self.interface
        self.group_data["sensor_type"] = self.sensor_type
        self.group_data["data_type"] = self.data_type
        self.group_data["delay_time"] = self.delay_time
        self.group_data["value_type"] = self.value_type
        self.group_data["command"] = self.command
        # self.valid[] = self.valid_max
        # self.valid[] = self.valid_min
        self.group_data["valid"] = self.valid
        self.sensor_meta = json.dumps(self.group_data, ensure_ascii=False, indent="\t")
        # print(sensor_meta)
        # return self.sensor_meta

    def write_json(self):
        # self.make_json()
        file_name = input('파일 이름을 입력해주세요(ex. test.json) :')
        with open(file_name, 'w', encoding="utf-8") as make_file:
            json.dump(self.group_data, make_file, ensure_ascii=False, indent="\t")
        print("jsonfile created")

    @staticmethod
    def load_json():
        with open('test.json')as json_file:
            json_data = json.load(json_file)
        print('Loaded data : ', json_data)
        return json_data


if __name__ == "__main__":
    a = regist()
    a.load_json()
