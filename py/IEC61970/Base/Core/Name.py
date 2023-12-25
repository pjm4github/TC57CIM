# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:03:56 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.NameType import NameType


class Name:
    """
    The Name class provides the means to define any number of human readable names
    for an object. A name is not to be used for defining inter-object
    relationships. For inter-object relationships instead use the object
    identification 'mRID'.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """

    def __init__(self) -> None:
        self.name: Optional[str] = ""   # Any free text that name the object.
        self.name_type: Optional[NameType] = NameType()  # Type of this name.
        self.identified_object: Optional[IdentifiedObject] = IdentifiedObject()  # Identified object that this name designates.


