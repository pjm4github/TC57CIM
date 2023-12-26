///////////////////////////////////////////////////////////
//  Voltage.h
//  Implementation of the Class Voltage
//  Created on:      25-Dec-2023 8:32:04 PM
///////////////////////////////////////////////////////////

#if !defined(EA_CFC42B17_B5DB_40aa_AB78_8C934C0C2BC7__INCLUDED_)
#define EA_CFC42B17_B5DB_40aa_AB78_8C934C0C2BC7__INCLUDED_

#include "UnitMultiplier.py"
#include "java\IEC61970\IEC61970\Base\Domain\UncefactUnitCode.java"
#include "UnitSymbol.py"
#include "Float.h"

/**
 * Electrical voltage, can be both AC and DC.
 */
class Voltage
{

public:
	Voltage();
	UnitMultiplier multiplier;
	UncefactUnitCode uncefactUnitCode;
	static const UnitSymbol unit;
	Float value;

};
#endif // !defined(EA_CFC42B17_B5DB_40aa_AB78_8C934C0C2BC7__INCLUDED_)
