from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ActivityRecord import ActivityRecord
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceEventType import EndDeviceEventType
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceEventDetail import EndDeviceEventDetail
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDevice import EndDevice
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint


class EndDeviceEvent(ActivityRecord):
    def __init__(self):
        super().__init__()
        self.issuer_id = ""  # Unique identifier of the business entity originating an end device control.
        self.issuer_tracking_id = ""  # Identifier assigned by the initiator (e.g. retail electric provider) of an end device control action to uniquely identify the demand response event, text message, or other subject of the control action.
        self.user_id = ""  # (if user initiated) ID of user who initiated this end device event.
        self.end_device_event_type = EndDeviceEventType()  # Type of this end device event.
        self.end_device_event_details = EndDeviceEventDetail()  # All details of this end device event.
        self.end_device = EndDevice()  # End device that reported this end device event.
        self.usage_point = UsagePoint()  # Usage point for which this end device event is reported.
