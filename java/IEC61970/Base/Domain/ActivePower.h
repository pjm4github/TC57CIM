///////////////////////////////////////////////////////////
//  ActivePower.h
//  Implementation of the Class ActivePower
//  Created on:      25-Dec-2023 8:31:54 PM
///////////////////////////////////////////////////////////

#if !defined(EA_A7D17530_083A_4c58_90D6_5EC78C27E698__INCLUDED_)
#define EA_A7D17530_083A_4c58_90D6_5EC78C27E698__INCLUDED_

#include "UnitMultiplier.py"
#include "java\IEC61970\IEC61970\Base\Domain\UncefactUnitCode.java"
#include "UnitSymbol.py"
#include "Float.h"

/**
 * Product of RMS value of the voltage and the RMS value of the in-phase component
 * of the current.
 */
class ActivePower
{

public:
	ActivePower();
	UnitMultiplier multiplier;
	UncefactUnitCode uncefactUnitCode;
	static const UnitSymbol unit;
	Float value;

};
#endif // !defined(EA_A7D17530_083A_4c58_90D6_5EC78C27E698__INCLUDED_)
