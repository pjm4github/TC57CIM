package IEC61970.Base.Meas;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * MeasurementValueSource describes the alternative sources updating a
 * MeasurementValue. User conventions for how to use the MeasurementValueSource
 * attributes are described in the introduction to IEC 61970-301.
 * @created 02-Jan-2024 11:20:34 PM
 */
public class MeasurementValueSource extends IdentifiedObject {

	/**
	 * The MeasurementValues updated by the source.
	 */
	public MeasurementValue MeasurementValues;

	public MeasurementValueSource(){

	}
}//end MeasurementValueSource