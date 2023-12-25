# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets import IEEEStandardEditionKind, IEEEStandardKind

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
        self.standard_edition = IEEEStandardEditionKind()
        self.standard_number = IEEEStandardKind()
