from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDevice import EndDevice
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceAction import EndDeviceAction
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceControlType import EndDeviceControlType
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceTiming import EndDeviceTiming
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePointGroup import UsagePointGroup
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.FloatQuantity import FloatQuantity


class EndDeviceControl(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.dr_program_level = 0  # Level of a demand response program request, where 0=emergency.
        self.dr_program_mandatory = True  # Whether a demand response program request is mandatory.
        self.issuer_id = ""  # Unique identifier of the business entity originating an end device control.
        self.issuer_tracking_id = ""  # Identifier assigned by the initiator (e.g. retail electric provider) of an end device control action to uniquely identify the demand response event, text message, or other subject of the control action.
        self.price_signal = FloatQuantity()  # (if applicable) Price signal used as parameter for this end device control.
        self.primary_device_timing = EndDeviceTiming()  # Timing for the control actions performed on the device identified in the end device control.
        self.reason = ""  # Reason for the control action that allows to determine how to continue processing.
        self.scheduled_interval = DateTimeInterval()  # (if control has scheduled duration) Date and time interval the control has been scheduled to execute within.
        self.secondary_device_timing = EndDeviceTiming()  # Timing for the control actions performed by devices that are responding to event related information sent to the primary device indicated in the end device control.
        self.usage_point_groups = [UsagePointGroup()]  # All usage point groups receiving commands from this end device control.
        self.end_devices = [EndDevice()]  # All end devices receiving commands from this end device control.
        self.end_device_action = EndDeviceAction()  # End device action issued by this end device control.
        self.end_device_control_type = EndDeviceControlType()  # Type of this end device control.
        self.usage_points = [UsagePoint()]  # All usage points receiving commands from this end device control.
