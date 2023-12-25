# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.ACDCTerminal import ACDCTerminal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.Equipment import Equipment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.OperationalLimits.OperationalLimit import OperationalLimit


class OperationalLimitSet(IdentifiedObject):
    """
    A set of limits associated with equipment. Sets of limits might apply to a specific temperature, or season for example.
    A set of limits may contain different severities of limit levels that would apply to the same equipment.
    The set may contain limits of different types such as apparent power and current limits or high and low voltage limits that are logically applied together as a set.
    @author: kdd
    @version: 1.0
    @created: 15-Dec-2023 4:38:28 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.equipment: Equipment = Equipment()
        self.terminal: ACDCTerminal = ACDCTerminal()
        self.operational_limit_value: OperationalLimit = OperationalLimit()
