///////////////////////////////////////////////////////////
//  PU.h
//  Implementation of the Class PU
//  Created on:      25-Dec-2023 8:32:02 PM
///////////////////////////////////////////////////////////

#if !defined(EA_F722205C_6FE0_4e5b_A805_0D1978025045__INCLUDED_)
#define EA_F722205C_6FE0_4e5b_A805_0D1978025045__INCLUDED_

#include "UnitMultiplier.py"
#include "UnitSymbol.py"
#include "Float.h"

/**
 * Per Unit - a positive or negative value referred to a defined base. Values
 * typically range from -10 to +10.
 */
class PU
{

public:
	PU();
	static const UnitMultiplier multiplier;
	static const UnitSymbol unit;
	Float value;

};
#endif // !defined(EA_F722205C_6FE0_4e5b_A805_0D1978025045__INCLUDED_)
