# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCEquipmentContainer import DCEquipmentContainer
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCConverterOperatingModeKind import DCConverterOperatingModeKind

class DCConverterUnit(DCEquipmentContainer):

    def __init__(self) -> None:
        super().__init__()
        self.operation_mode: DCConverterOperatingModeKind = DCConverterOperatingModeKind.MONOPOLAR_GROUND_RETURN
