package IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Field voltage over excitation limiter.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OverexcLimX1 extends OverexcitationLimiterDynamics {

	/**
	 * Low voltage point on the inverse time characteristic (EFD<sub>1</sub>).
	 * Typical Value = 1.1.
	 */
	public PU efd1;
	/**
	 * Mid voltage point on the inverse time characteristic (EFD<sub>2</sub>).
	 * Typical Value = 1.2.
	 */
	public PU efd2;
	/**
	 * High voltage point on the inverse time characteristic (EFD<sub>3</sub>).
	 * Typical Value = 1.5.
	 */
	public PU efd3;
	/**
	 * Desired field voltage (EFD<sub>DES</sub>).  Typical Value = 0.9.
	 */
	public PU efddes;
	/**
	 * Rated field voltage (EFD<sub>RATED</sub>).  Typical Value = 1.05.
	 */
	public PU efdrated;
	/**
	 * Gain (K<sub>MX</sub>).  Typical Value = 0.01.
	 */
	public PU kmx;
	/**
	 * Time to trip the exciter at the low voltage point on the inverse time
	 * characteristic (TIME<sub>1</sub>).  Typical Value = 120.
	 */
	public Seconds t1;
	/**
	 * Time to trip the exciter at the mid voltage point on the inverse time
	 * characteristic (TIME<sub>2</sub>).  Typical Value = 40.
	 */
	public Seconds t2;
	/**
	 * Time to trip the exciter at the high voltage point on the inverse time
	 * characteristic (TIME<sub>3</sub>).  Typical Value = 15.
	 */
	public Seconds t3;
	/**
	 * Low voltage limit (V<sub>LOW</sub>) (>0).
	 */
	public PU vlow;

	public OverexcLimX1(){

	}
}//end OverexcLimX1