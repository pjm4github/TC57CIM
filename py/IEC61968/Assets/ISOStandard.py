# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.ISOStandardEditionKind import ISOStandardEditionKind
from IEC61968.Assets.ISOStandardKind import ISOStandardKind


class ISOStandard:
    def __init__(self):
        self.standard_edition = ISOStandardEditionKind.UNKNOWN
        self.standard_number = ISOStandardKind.DETERMINATION_OF_FLASH_POINT
