package IEC62325.Environmental;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;

/**
 * A tsunami (tidal wave), a long high sea wave caused by an earthquake, submarine
 * landslide, or other disturbance.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class Tsunami extends HydrosphericPhenomenon {

	/**
	 * Tsunami intensity on the Papadopoulos-Imamura tsunami intensity scale. Possible
	 * values are 1-12, corresponding to I-XII.
	 */
	public Integer intensity;
	/**
	 * Tsunami magnitude in the Tsunami Magnitude Scale (Mt).  Is greater than zero.
	 */
	public Float magnitude;

	public Tsunami(){

	}
}//end Tsunami