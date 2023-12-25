# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:03:56 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.NameTypeAuthority import NameTypeAuthority


class NameType:
    """
    Type of name. Possible values for attribute 'name' are implementation dependent
    but standard profiles may specify types. An enterprise may have multiple IT
    systems each having its own local name for the same object, e.g. a planning
    system may have different names from an EMS. An object may also have different
    names within the same IT system, e.g. localName as defined in CIM version 14.
    The definition from CIM14 is:
    The localName is a human readable name of the object. It is a free text name
    local to a node in a naming hierarchy similar to a file directory structure. A
    power system related naming hierarchy may be: Substation, VoltageLevel,
    Equipment etc. Children of the same parent in such a hierarchy have names that
    typically are unique among them.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """

    def __init__(self) -> None:
        self.description: Optional[str] = ""  # Description of the name type
        self.name: Optional[str] = ""  # Name of the name type
        self.name_type_authority: Optional[NameTypeAuthority] = NameTypeAuthority()  # Authority responsible for managing names of this type

