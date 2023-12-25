
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.CustomerAgreement import CustomerAgreement
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceEvent import EndDeviceEvent


class MeterReading(IdentifiedObject):
    #  * Set of values obtained from the meter.
    #  * @created 20-Dec-2023 6:25:51 PM
    def __init__(self):
        super().__init__()
        self.is_coincident_trigger = True  # If true, this meter reading is the meter reading for which other coincident meter readings are requested or provided.
        self.values_interval = DateTimeInterval()  # Date and time interval of the data items contained within this meter reading.
        self.usage_point = UsagePoint()  # Usage point from which this meter reading (set of values) has been obtained.
        self.end_device_events = EndDeviceEvent()  # All end device events associated with this set of measured values.
        self.customer_agreement = CustomerAgreement()  # (could be deprecated in the future) Customer agreement for this meter reading.
