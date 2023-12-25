# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.TAPPIStandardEditionKind import TAPPIStandardEditionKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.TAPPIStandardKind import TAPPIStandardKind


class TAPPIStandard:

    def __init__(self):
        self.standard_edition = TAPPIStandardEditionKind.NONE
        self.standard_number = TAPPIStandardKind.T494
