# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from IEC61970.Base.DC.ACDCConverter import ACDCConverter
from IEC61970.Base.DC.DCPolarityKind import DCPolarityKind
from IEC61970.Base.DC.DCBaseTerminal import DCBaseTerminal


class AcdcConverterDcTerminal(DCBaseTerminal):

    def __init__(self) -> None:
        super().__init__()
        self.polarity: DCPolarityKind.POSITIVE  # Represents the normal network polarity condition.
        self.dc_conducting_equipment: ACDCConverter = ACDCConverter()  # A DC converter terminal belong to
        # an DC converter.
