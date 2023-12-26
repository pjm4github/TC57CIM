package IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents the Type UEL1 model which has a circular limit boundary
 * when plotted in terms of machine reactive power vs. real power output.
 * 
 * Reference: IEEE UEL1 421.5-2005 Section 10.1.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class UnderexcLimIEEE1 extends UnderexcitationLimiterDynamics {

	/**
	 * UEL center setting (K<sub>UC</sub>).  Typical Value = 1.38.
	 */
	public PU kuc;
	/**
	 * UEL excitation system stabilizer gain (K<sub>UF</sub>).  Typical Value = 3.3.
	 */
	public PU kuf;
	/**
	 * UEL integral gain (K<sub>UI</sub>).  Typical Value = 0.
	 */
	public PU kui;
	/**
	 * UEL proportional gain (K<sub>UL</sub>).  Typical Value = 100.
	 */
	public PU kul;
	/**
	 * UEL radius setting (K<sub>UR</sub>).  Typical Value = 1.95.
	 */
	public PU kur;
	/**
	 * UEL lead time constant (T<sub>U1</sub>).  Typical Value = 0.
	 */
	public Seconds tu1;
	/**
	 * UEL lag time constant (T<sub>U2</sub>).  Typical Value = 0.05.
	 */
	public Seconds tu2;
	/**
	 * UEL lead time constant (T<sub>U3</sub>).  Typical Value = 0.
	 */
	public Seconds tu3;
	/**
	 * UEL lag time constant (T<sub>U4</sub>).  Typical Value = 0.
	 */
	public Seconds tu4;
	/**
	 * UEL maximum limit for operating point phasor magnitude (V<sub>UCMAX</sub>).
	 * Typical Value = 5.8.
	 */
	public PU vucmax;
	/**
	 * UEL integrator output maximum limit (V<sub>UIMAX</sub>).
	 */
	public PU vuimax;
	/**
	 * UEL integrator output minimum limit (V<sub>UIMIN</sub>).
	 */
	public PU vuimin;
	/**
	 * UEL output maximum limit (V<sub>ULMAX</sub>).  Typical Value = 18.
	 */
	public PU vulmax;
	/**
	 * UEL output minimum limit (V<sub>ULMIN</sub>).  Typical Value = -18.
	 */
	public PU vulmin;
	/**
	 * UEL maximum limit for radius phasor magnitude (V<sub>URMAX</sub>).  Typical
	 * Value = 5.8.
	 */
	public PU vurmax;

	public UnderexcLimIEEE1(){

	}
}//end UnderexcLimIEEE1