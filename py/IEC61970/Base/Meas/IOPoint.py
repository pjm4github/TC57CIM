# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:38:50 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.ICCPConfiguration.ProvidedBilateralPoint import ProvidedBilateralPoint


class IOPoint(IdentifiedObject):
    """The class describe a measurement or control value. The purpose is to enable
    having attributes and associations common for measurement and control.
    """
    def __init__(self) -> None:
        super().__init__()
        self.bilateral_to_io_point: ProvidedBilateralPoint = ProvidedBilateralPoint()
