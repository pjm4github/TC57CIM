from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class ActivePowerPerFrequency:
    """
    ///////////////////////////////////////////////////////////
    //  ActivePowerPerFrequency.cpp
    //  Implementation of the Class ActivePowerPerFrequency
    //  Created on:      16-Dec-2023 8:48:27 PM
    ///////////////////////////////////////////////////////////
    """
    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0

    unit = UnitSymbol.none
