# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceGroup import EndDeviceGroup


class DerFunction:
    def __init__(self):
        self.connect_disconnect = False
        self.frequency_watt_curve_function = False
        self.max_real_power_limiting = False
        self.ramp_rate_control = False
        self.reactive_power_dispatch = False
        self.real_power_dispatch = False
        self.voltage_regulation = False
        self.volt_var_curve_function = False
        self.volt_watt_curve_function = False
        self.end_device_group = EndDeviceGroup()
