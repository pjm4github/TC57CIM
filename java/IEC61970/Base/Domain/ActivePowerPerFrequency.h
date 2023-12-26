///////////////////////////////////////////////////////////
//  ActivePowerPerFrequency.h
//  Implementation of the Class ActivePowerPerFrequency
//  Created on:      25-Dec-2023 8:31:54 PM
///////////////////////////////////////////////////////////

#if !defined(EA_878A25A2_D9B3_4f70_8EBB_AAF4E8095230__INCLUDED_)
#define EA_878A25A2_D9B3_4f70_8EBB_AAF4E8095230__INCLUDED_

#include "UnitMultiplier.py"
#include "UnitSymbol.py"
#include "Float.h"

/**
 * Active power variation with frequency.
 */
class ActivePowerPerFrequency
{

public:
	ActivePowerPerFrequency();
	UnitMultiplier multiplier;
	static const UnitSymbol unit;
	Float value;

};
#endif // !defined(EA_878A25A2_D9B3_4f70_8EBB_AAF4E8095230__INCLUDED_)
