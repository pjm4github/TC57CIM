///////////////////////////////////////////////////////////
//  MeasurementValue.h
//  Implementation of the Class MeasurementValue
//  Created on:      25-Dec-2023 8:32:00 PM
///////////////////////////////////////////////////////////

#if !defined(EA_81827EC9_EED0_4902_BE7C_8E1E6C28D77B__INCLUDED_)
#define EA_81827EC9_EED0_4902_BE7C_8E1E6C28D77B__INCLUDED_

#include "PerCent.py"
#include "DateTime.py"
#include "RemoteSource.py"
#include "IOPoint.py"
#include "MeasurementValueExt.h"
#include "MeasurementValueQuality.h"

/**
 * The current state for a measurement. A state value is an instance of a
 * measurement from a specific source. Measurements can be associated with many
 * state values, each representing a different source for the measurement.
 */
class MeasurementValue : public IOPoint, public MeasurementValueExt
{

public:
	MeasurementValue();
	/**
	 * The limit, expressed as a percentage of the sensor maximum, that errors will
	 * not exceed when the sensor is used under  reference conditions.
	 */
	PerCent sensorAccuracy;
	/**
	 * The time when the value was last updated
	 */
	DateTime timeStamp;
	/**
	 * Link to the physical telemetered point associated with this measurement.
	 */
	RemoteSource *RemoteSource;
	/**
	 * A MeasurementValue has a MeasurementValueQuality associated with it.
	 */
	MeasurementValueQuality *MeasurementValueQuality;

};
#endif // !defined(EA_81827EC9_EED0_4902_BE7C_8E1E6C28D77B__INCLUDED_)
