///////////////////////////////////////////////////////////
//  IrregularIntervalSchedule.h
//  Implementation of the Class IrregularIntervalSchedule
//  Created on:      25-Dec-2023 8:31:59 PM
///////////////////////////////////////////////////////////

#if !defined(EA_40868CFE_6164_4b11_838B_C683C8E81286__INCLUDED_)
#define EA_40868CFE_6164_4b11_838B_C683C8E81286__INCLUDED_

#include "BasicIntervalSchedule.py"
#include "IrregularTimePoint.h"

/**
 * The schedule has time points where the time between them varies.
 */
class IrregularIntervalSchedule : public BasicIntervalSchedule
{

public:
	IrregularIntervalSchedule();
	/**
	 * The point data values that define a curve.
	 */
	IrregularTimePoint *TimePoints;

};
#endif // !defined(EA_40868CFE_6164_4b11_838B_C683C8E81286__INCLUDED_)
