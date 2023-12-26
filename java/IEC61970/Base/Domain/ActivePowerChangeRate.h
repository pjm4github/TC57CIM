///////////////////////////////////////////////////////////
//  ActivePowerChangeRate.h
//  Implementation of the Class ActivePowerChangeRate
//  Created on:      25-Dec-2023 8:31:54 PM
///////////////////////////////////////////////////////////

#if !defined(EA_9317D075_0021_4bf7_AC8E_5372FAD66BB5__INCLUDED_)
#define EA_9317D075_0021_4bf7_AC8E_5372FAD66BB5__INCLUDED_

#include "UnitMultiplier.py"
#include "UnitSymbol.py"
#include "Float.h"

/**
 * Rate of change of active power per time.
 */
class ActivePowerChangeRate
{

public:
	ActivePowerChangeRate();
	UnitMultiplier multiplier;
	static const UnitSymbol unit;
	Float value;

};
#endif // !defined(EA_9317D075_0021_4bf7_AC8E_5372FAD66BB5__INCLUDED_)
