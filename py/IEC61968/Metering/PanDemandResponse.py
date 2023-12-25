# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceAction import EndDeviceAction
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Temperature import Temperature


class PanDemandResponse(EndDeviceAction):

    def __init__(self):
        super().__init__()
        self.appliance = None  # Appliance being controlled.
        self.avg_load_adjustment = PerCent()  # Used to define a maximum energy usage limit as a percentage of the client
        self.cancel_control_mode = ""  # Encoding of cancel control.
        self.cancel_date_time = DateTime()  # Timestamp when a canceling of the event is scheduled to start.
        self.cancel_now = False  # If true, a canceling of the event should start immediately.
        self.cooling_offset = Temperature()  # Requested offset to apply to the normal cooling setpoint at the time of the
        self.cooling_setpoint = Temperature()  # Requested cooling set point.
        self.criticality_level = ""  # Level of criticality for the action of this control.
        self.duty_cycle = PerCent()  # Maximum "on" state duty cycle as a percentage of time.
        self.enrollment_group = ""  # Provides a mechanism to direct load control actions to groups of PAN devices.
        self.heating_offset = Temperature()  # Requested offset to apply to the normal heating setpoint at the time of the
        self.heating_setpoint = Temperature()  # Requested heating set point.
