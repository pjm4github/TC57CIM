///////////////////////////////////////////////////////////
//  Analog.h
//  Implementation of the Class Analog
//  Created on:      25-Dec-2023 8:31:54 PM
///////////////////////////////////////////////////////////

#if !defined(EA_1D383E95_0547_4538_9D2F_7815CC7F20DF__INCLUDED_)
#define EA_1D383E95_0547_4538_9D2F_7815CC7F20DF__INCLUDED_

#include "Float.h"
#include "Boolean.h"
#include "AnalogValue.py"
#include "Measurement.py"
#include "AnalogLimitSet.py"

/**
 * Analog represents an analog Measurement.
 */
class Analog : public Measurement
{

public:
	Analog();
	/**
	 * Normal value range maximum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	Float maxValue;
	/**
	 * Normal value range minimum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	Float minValue;
	/**
	 * Normal measurement value, e.g., used for percentage calculations.
	 */
	Float normalValue;
	/**
	 * If true then this measurement is an active power, reactive power or current
	 * with the convention that a positive value measured at the Terminal means power
	 * is flowing into the related PowerSystemResource.
	 */
	Boolean positiveFlowIn;
	/**
	 * The values connected to this measurement.
	 */
	AnalogValue *AnalogValues;
	/**
	 * A measurement may have zero or more limit ranges defined for it.
	 */
	AnalogLimitSet *LimitSets;

};
#endif // !defined(EA_1D383E95_0547_4538_9D2F_7815CC7F20DF__INCLUDED_)
