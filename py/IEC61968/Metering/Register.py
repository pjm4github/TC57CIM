from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.TimeInterval import TimeInterval
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.Channel import Channel
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction


class Register(IdentifiedObject):
    def __init__(self):
        self.is_virtual = False  # If true, the data it produces is calculated or measured by a device other than a physical end device/meter. Otherwise, any data streams it produces are measured by the hardware of the end device/meter itself.
        self.left_digit_count = 0  # Number of digits (dials on a mechanical meter) to the left of the decimal place; default is normally 5.
        self.right_digit_count = 0  # Number of digits (dials on a mechanical meter) to the right of the decimal place.
        self.tou_tier = TimeInterval()  # Clock time interval for register to begin/cease accumulating time of usage (e.g., start at 8:00 am, stop at 5:00 pm).
        self.tou_tier_name = ""  # Name used for the time of use tier (also known as bin or bucket). For example, "peak", "off-peak", "TOU Category A", etc.
        self.channels = [Channel()]  # All channels that collect/report values from this register.
        self.end_device_function = EndDeviceFunction()  # End device function metering quantities displayed by this register.
