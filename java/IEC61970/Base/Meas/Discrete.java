package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Integer;

/**
 * Discrete represents a discrete Measurement, i.e. a Measurement representing
 * discrete values, e.g. a Breaker position.
 * @created 02-Jan-2024 11:18:26 PM
 */
public class Discrete extends Measurement {

	/**
	 * Normal value range maximum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	public Integer maxValue;
	/**
	 * Normal value range minimum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	public Integer minValue;
	/**
	 * Normal measurement value, e.g., used for percentage calculations.
	 */
	public Integer normalValue;
	/**
	 * The values connected to this measurement.
	 */
	public DiscreteValue DiscreteValues;

	public Discrete(){

	}
}//end Discrete