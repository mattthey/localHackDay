import re

class Data:
    _values = dict()
    _alarms = []
    _regexpt_for_name = re.compile(r'\d?[PT]\w{1,2}\d_1_Q')
    _is_file_correct = False
    _regexp_for_parse = re.compile(r"(\d{2}.\d{2}.\d{4}\s\d{2}:\d{2}:\d{2}.0)\s+\??\s+(\d?\S+)\s+TC5\s+=(-?\d+.?\d*)\s+\w+.")

    def get_file_correctness(self):
        return self._is_file_correct

    def _parce_line(self, line):
        result = re.findall(self._regexp_for_parse, line)
        if len(result) == 0:
            return None
        return result[0]

    def _is_last_line_in_log(self, line):
        return "STOP" in line

    def __init__(self, file_name):
        self._is_file_correct = False
        with open(file_name, 'r') as f:
            f.readline()
            while True:
                line = f.readline()
                if self._is_last_line_in_log(line):
                    break
                parsed_line = self._parce_line(line)
                if parsed_line is None:
                    return
                self._add_value(*parsed_line)
            self._is_file_correct = True


    def _is_name_from_sensor(self, name):
        return re.match(self._regexpt_for_name, name)

    def _add_value(self, time, name, value):
        if self._is_name_from_sensor(name):
            if name not in self._values.keys():
                self._values[name] = []
            self._values[name].append((time, value))
        else:
            self._alarms.append((time, name))

    def get_alarms(self):
        return self._alarms

    def get_sensor_names(self):
        return list(self._values.keys())

    def get_sensor_values(self, sensor_name):
        if sensor_name in self.get_sensor_names():
            return self._values[sensor_name]
        raise ValueError("Sensor not found")