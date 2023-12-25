
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetInfo import AssetInfo
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceCapability import EndDeviceCapability
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage


class EndDeviceInfo(AssetInfo):
    def __init__(self):
        super().__init__()
        self.capability = EndDeviceCapability()  # Inherent capabilities of the device (i.e., the functions it supports).
        self.isSolidState = False  # If true, this is a solid state end device (as opposed to a mechanical or electromechanical device).
        self.phaseCount = 0  # Number of potential phases the end device supports, typically 0, 1 or 3.
        self.ratedCurrent = CurrentFlow()  # Rated current.
        self.ratedVoltage = Voltage()  # Rated voltage.
