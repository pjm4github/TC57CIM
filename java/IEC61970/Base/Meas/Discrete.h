///////////////////////////////////////////////////////////
//  Discrete.h
//  Implementation of the Class Discrete
//  Created on:      25-Dec-2023 8:31:56 PM
///////////////////////////////////////////////////////////

#if !defined(EA_441CAC08_50A6_4f4e_AC94_443176E084BB__INCLUDED_)
#define EA_441CAC08_50A6_4f4e_AC94_443176E084BB__INCLUDED_

#include "Integer.h"
#include "Measurement.py"
#include "DiscreteValue.h"

/**
 * Discrete represents a discrete Measurement, i.e. a Measurement representing
 * discrete values, e.g. a Breaker position.
 */
class Discrete : public Measurement
{

public:
	Discrete();
	/**
	 * Normal value range maximum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	Integer maxValue;
	/**
	 * Normal value range minimum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	Integer minValue;
	/**
	 * Normal measurement value, e.g., used for percentage calculations.
	 */
	Integer normalValue;
	/**
	 * The values connected to this measurement.
	 */
	DiscreteValue *DiscreteValues;

};
#endif // !defined(EA_441CAC08_50A6_4f4e_AC94_443176E084BB__INCLUDED_)
