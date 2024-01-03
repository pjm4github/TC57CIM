package IEC61970.Base.Meas;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;

/**
 * Analog represents an analog Measurement.
 * @created 02-Jan-2024 11:17:21 PM
 */
public class Analog extends Measurement {

	/**
	 * Normal value range maximum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	public Float maxValue;
	/**
	 * Normal value range minimum for any of the MeasurementValue.values. Used for
	 * scaling, e.g. in bar graphs or of telemetered raw values.
	 */
	public Float minValue;
	/**
	 * Normal measurement value, e.g., used for percentage calculations.
	 */
	public Float normalValue;
	/**
	 * If true then this measurement is an active power, reactive power or current
	 * with the convention that a positive value measured at the Terminal means power
	 * is flowing into the related PowerSystemResource.
	 */
	public Boolean positiveFlowIn;
	/**
	 * The values connected to this measurement.
	 */
	public AnalogValue AnalogValues;
	/**
	 * A measurement may have zero or more limit ranges defined for it.
	 */
	public AnalogLimitSet LimitSets;

	public Analog(){

	}
}//end Analog