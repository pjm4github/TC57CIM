///////////////////////////////////////////////////////////
//  IrregularTimePoint.h
//  Implementation of the Class IrregularTimePoint
//  Created on:      25-Dec-2023 8:31:59 PM
///////////////////////////////////////////////////////////

#if !defined(EA_F5EAE55B_E3AA_4401_820D_FF8C198B0D4D__INCLUDED_)
#define EA_F5EAE55B_E3AA_4401_820D_FF8C198B0D4D__INCLUDED_

#include "Seconds.py"
#include "Float.h"

/**
 * TimePoints for a schedule where the time between the points varies.
 */
class IrregularTimePoint
{

public:
	IrregularTimePoint();
	/**
	 * The time is relative to the schedule starting time.
	 */
	Seconds time;
	/**
	 * The first value at the time. The meaning of the value is defined by the derived
	 * type of the associated schedule.
	 */
	Float value1;
	/**
	 * The second value at the time. The meaning of the value is defined by the
	 * derived type of the associated schedule.
	 */
	Float value2;

};
#endif // !defined(EA_F5EAE55B_E3AA_4401_820D_FF8C198B0D4D__INCLUDED_)
