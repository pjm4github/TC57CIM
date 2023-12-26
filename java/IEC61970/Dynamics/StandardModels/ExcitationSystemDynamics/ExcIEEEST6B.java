package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type ST6B model. This model consists
 * of a PI voltage regulator with an inner loop field voltage regulator and pre-
 * control. The field voltage regulator implements a proportional control. The pre-
 * control and the delay in the feedback circuit increase the dynamic response.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 7.6.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEST6B extends ExcitationSystemDynamics {

	/**
	 * Exciter output current limit reference (I<sub>LR</sub>).  Typical Value = 4.164.
	 */
	public PU ilr;
	/**
	 * Exciter output current limit adjustment (K<sub>CI</sub>).  Typical Value = 1.
	 * 0577.
	 */
	public PU kci;
	/**
	 * Pre-control gain constant of the inner loop field regulator (K<sub>FF</sub>).
	 * Typical Value = 1.
	 */
	public PU kff;
	/**
	 * Feedback gain constant of the inner loop field regulator (K<sub>G</sub>).
	 * Typical Value = 1.
	 */
	public PU kg;
	/**
	 * Voltage regulator integral gain (K<sub>IA</sub>).  Typical Value = 45.094.
	 */
	public PU kia;
	/**
	 * Exciter output current limiter gain (K<sub>LR</sub>).  Typical Value = 17.33.
	 */
	public PU klr;
	/**
	 * Forward gain constant of the inner loop field regulator (K<sub>M</sub>).
	 * Typical Value = 1.
	 */
	public PU km;
	/**
	 * Voltage regulator proportional gain (K<sub>PA</sub>).  Typical Value = 18.038.
	 */
	public PU kpa;
	/**
	 * OEL input selector (OELin). Typical Value = noOELinput.
	 */
	public ExcST6BOELselectorKind oelin;
	/**
	 * Feedback time constant of inner loop field voltage regulator (T<sub>G</sub>).
	 * Typical Value = 0.02.
	 */
	public Seconds tg;
	/**
	 * Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 4.81.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -3.85.
	 */
	public PU vamin;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 4.81.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -3.85.
	 */
	public PU vrmin;

	public ExcIEEEST6B(){

	}
}//end ExcIEEEST6B