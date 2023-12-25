# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceGroup import EndDeviceGroup
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class DerGroupForecast(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.prediction_creation_date = DateTime()
        self.end_device_group = EndDeviceGroup()
