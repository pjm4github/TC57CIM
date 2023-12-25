# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:03:56 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core import IdentifiedObject
from typing import Any

class OperatingParticipant(IdentifiedObject):
    """An operator of multiple power system resource objects. Note multiple operating
    participants may operate the same power system resource object. This can be
    used for modeling jointly owned units where each owner operates as a
    contractual share.
    @author: kdd
    @version: 1.0
    @created: 15-Dec-2023 4:38:28 PM
    """

    def __init__(self) -> None:
        super().__init__()
    
