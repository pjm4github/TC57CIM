package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.RelativeDisplacement;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;

/**
 * An earthquake.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class Earthquake extends GeosphericPhenomenon {

	/**
	 * The depth below the earth's surface of the earthquake's focal point.
	 */
	public RelativeDisplacement focalDepth;
	/**
	 * The intensity of the earthquake as defined by the Modified Mercalli Intensity
	 * (MMI) scale. Possible values are 1-12, corresponding to I-XII.
	 */
	public Integer intensity;
	/**
	 * The magnitude of the earthquake as defined on the Moment Magnitude
	 * (M<sub>w</sub>) scale, which measures the size of earthquakes in terms of the
	 * energy released. Must be greater than zero.
	 */
	public Float magnitude;

	public Earthquake(){

	}
}//end Earthquake