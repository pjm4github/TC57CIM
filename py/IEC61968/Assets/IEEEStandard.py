# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from IEC61968.Assets.IEEEStandardEditionKind import IEEEStandardEditionKind
from IEC61968.Assets.IEEEStandardKind import IEEEStandardKind
class IEEEStandard:
    """
    Standard published by IEEE (Institute of Electrical and Electronics Engineers)
    
    @author ppbr003
    @version 1.0
    @created 19-Dec-2023 10:34:36 AM
    """

    def __init__(self):
        """
        Constructor for IEEEStandard
        """
        self.standard_edition = IEEEStandardEditionKind.m_1995
        self.standard_number = IEEEStandardKind.IEEE_GUIDE_FOR_DIAGNOSTIC_FIELD_TESTING
