# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.SubGeographicalRegion import SubGeographicalRegion
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCEquipmentContainer import DCEquipmentContainer


class DCLine(DCEquipmentContainer):
    """
    Overhead lines and/or cables connecting two or more HVDC substations.
    @author selaost1
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """
    def __init__(self) -> None:
        """
        The SubGeographicalRegion containing the DC line.
        """
        super().__init__()
        self.region: SubGeographicalRegion = SubGeographicalRegion()

