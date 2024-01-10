# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# from IEC61968.Assets.WEPStandardEditionKind import WEPStandardEditionKind
# from IEC61968.Assets.WEPStandardKind import WEPStandardKind
from IEC61968.Assets.WEPStandardEditionKind import WEPStandardEditionKind
from IEC61968.Assets.WEPStandardKind import WEPStandardKind


class WEPStandard:
    def __init__(self):
        self.standard_edition = WEPStandardEditionKind.NONE
        self.standard_number = WEPStandardKind.WEP_12_1254E
