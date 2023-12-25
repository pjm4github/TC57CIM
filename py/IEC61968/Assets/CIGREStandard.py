# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.CIGREStandardEditionKind import CIGREStandardEditionKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.CIGREStandardKind import CIGREStandardKind


class CIGREStandard:
    """
    Standard published by CIGRE (Council on Large Electric Systems).
    """
    
    def __init__(self):
        """
        Constructor for CIGREStandard class
        """
        self.standard_edition = CIGREStandardEditionKind.NONE
        self.standard_number = CIGREStandardKind.TB_170
