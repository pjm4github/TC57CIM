///////////////////////////////////////////////////////////
//  AccumulatorValue.h
//  Implementation of the Class AccumulatorValue
//  Created on:      25-Dec-2023 8:31:54 PM
///////////////////////////////////////////////////////////

#if !defined(EA_6F382D00_8DA5_4165_B3E5_350F41E09120__INCLUDED_)
#define EA_6F382D00_8DA5_4165_B3E5_350F41E09120__INCLUDED_

#include "Integer.h"
#include "MeasurementValue.h"

/**
 * AccumulatorValue represents an accumulated (counted) MeasurementValue.
 */
class AccumulatorValue : public MeasurementValue
{

public:
	AccumulatorValue();
	/**
	 * The value to supervise. The value is positive.
	 */
	Integer value;

};
#endif // !defined(EA_6F382D00_8DA5_4165_B3E5_350F41E09120__INCLUDED_)
