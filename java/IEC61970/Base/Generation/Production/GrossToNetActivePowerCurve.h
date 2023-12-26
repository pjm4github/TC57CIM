///////////////////////////////////////////////////////////
//  GrossToNetActivePowerCurve.h
//  Implementation of the Class GrossToNetActivePowerCurve
//  Created on:      25-Dec-2023 8:31:59 PM
///////////////////////////////////////////////////////////

#if !defined(EA_B0F2CB9C_5485_482e_A616_2C6F7AC7E297__INCLUDED_)
#define EA_B0F2CB9C_5485_482e_A616_2C6F7AC7E297__INCLUDED_

#include "Curve.py"

/**
 * Relationship between the generating unit's gross active power output on the X-
 * axis (measured at the terminals of the machine(s)) and the generating unit's
 * net active power output on the Y-axis (based on utility-defined measurements at
 * the power station). Station service loads, when modeled, should be treated as
 * non-conforming bus loads. There may be more than one curve, depending on the
 * auxiliary equipment that is in service.
 */
class GrossToNetActivePowerCurve : public Curve
{

public:
	GrossToNetActivePowerCurve();

};
#endif // !defined(EA_B0F2CB9C_5485_482e_A616_2C6F7AC7E297__INCLUDED_)
