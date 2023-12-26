///////////////////////////////////////////////////////////
//  ActivePowerPerCurrentFlow.h
//  Implementation of the Class ActivePowerPerCurrentFlow
//  Created on:      25-Dec-2023 8:31:54 PM
//  Original author: 222206
///////////////////////////////////////////////////////////

#if !defined(EA_DD4B56AD_E99E_435c_B2A8_2A7F43828609__INCLUDED_)
#define EA_DD4B56AD_E99E_435c_B2A8_2A7F43828609__INCLUDED_

#include "UnitMultiplier.py"
#include "UnitSymbol.py"
#include "Float.h"

class ActivePowerPerCurrentFlow
{

public:
	ActivePowerPerCurrentFlow();
	UnitMultiplier multiplier;
	static const UnitSymbol unit;
	Float value;

};
#endif // !defined(EA_DD4B56AD_E99E_435c_B2A8_2A7F43828609__INCLUDED_)
