package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Integer;

/**
 * Accumulator represents an accumulated (counted) Measurement, e.g. an energy
 * value.
 * @created 03-Jan-2024 4:14:57 PM
 */
public class Accumulator extends Measurement {

	/**
	 * Normal value range maximum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	public Integer maxValue;
	/**
	 * The values connected to this measurement.
	 */
	public AccumulatorValue AccumulatorValues;
	/**
	 * A measurement may have zero or more limit ranges defined for it.
	 */
	public AccumulatorLimitSet LimitSets;

	public Accumulator(){

	}
}//end Accumulator