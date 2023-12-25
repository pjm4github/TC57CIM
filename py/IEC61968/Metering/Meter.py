# Meter.py
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDevice import EndDevice
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.MeterMultiplier import MeterMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.MeterReading import MeterReading


class Meter(EndDevice):
    """
    Physical asset that performs the metering role of the usage point. Used for
    measuring consumption and detection of events.
    """

    def __init__(self):
        super().__init__()
        self.form_number = ""  # Meter form designation per ANSI C12.10 or other applicable standard. An alphanumeric designation denoting the circuit arrangement for which the meter is applicable and its specific terminal arrangement.
        self.meter_multipliers = MeterMultiplier()  # All multipliers applied at this meter.
        self.meter_readings = MeterReading()  # All meter readings provided by this meter.