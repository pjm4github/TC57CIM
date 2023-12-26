package IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * Field Voltage or Current overexcitation limiter designed to protect the
 * generator field of an AC machine with automatic excitation control from
 * overheating due to prolonged overexcitation.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OverexcLimX2 extends OverexcitationLimiterDynamics {

	/**
	 * Low voltage or current point on the inverse time characteristic
	 * (EFD<sub>1</sub>).  Typical Value = 1.1.
	 */
	public PU efd1;
	/**
	 * Mid voltage or current point on the inverse time characteristic
	 * (EFD<sub>2</sub>).  Typical Value = 1.2.
	 */
	public PU efd2;
	/**
	 * High voltage or current point on the inverse time characteristic
	 * (EFD<sub>3</sub>).  Typical Value = 1.5.
	 */
	public PU efd3;
	/**
	 * Desired field voltage if m=F or field current if m=T (EFD<sub>DES</sub>).
	 * Typical Value = 1.
	 */
	public PU efddes;
	/**
	 * Rated field voltage if m=F or field current if m=T (EFD<sub>RATED</sub>).
	 * Typical Value = 1.05.
	 */
	public PU efdrated;
	/**
	 * Gain (K<sub>MX</sub>).  Typical Value = 0.002.
	 */
	public PU kmx;
	/**
	 * (m).
	 * true = IFD limiting
	 * false = EFD limiting.
	 */
	public Boolean m;
	/**
	 * Time to trip the exciter at the low voltage or current point on the inverse
	 * time characteristic (TIME<sub>1</sub>).  Typical Value = 120.
	 */
	public Seconds t1;
	/**
	 * Time to trip the exciter at the mid voltage or current point on the inverse
	 * time characteristic (TIME<sub>2</sub>).  Typical Value = 40.
	 */
	public Seconds t2;
	/**
	 * Time to trip the exciter at the high voltage or current point on the inverse
	 * time characteristic (TIME<sub>3</sub>).  Typical Value = 15.
	 */
	public Seconds t3;
	/**
	 * Low voltage limit (V<sub>LOW</sub>) (>0).
	 */
	public PU vlow;

	public OverexcLimX2(){

	}
}//end OverexcLimX2