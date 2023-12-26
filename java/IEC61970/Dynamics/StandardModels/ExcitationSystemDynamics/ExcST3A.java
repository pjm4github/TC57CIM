package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.AngleDegrees;

/**
 * Modified IEEE ST3A static excitation system with added speed multiplier.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcST3A extends ExcitationSystemDynamics {

	/**
	 * Maximum AVR output (Efdmax).  Typical Value = 6.9.
	 */
	public PU efdmax;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc). Typical
	 * Value = 1.1.
	 */
	public PU kc;
	/**
	 * Feedback gain constant of the inner loop field regulator (Kg).  Typical Value =
	 * 1.
	 */
	public PU kg;
	/**
	 * Potential circuit gain coefficient (Ki).  Typical Value = 4.83.
	 */
	public PU ki;
	/**
	 * AVR gain (Kj).  Typical Value = 200.
	 */
	public PU kj;
	/**
	 * Forward gain constant of the inner loop field regulator (Km).  Typical Value =
	 * 7.04.
	 */
	public PU km;
	/**
	 * Potential source gain (Kp) (>0).  Typical Value = 4.37.
	 */
	public PU kp;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks1).
	 * Typical Value = 0.
	 */
	public PU ks1;
	/**
	 * Voltage regulator time constant (Tb).  Typical Value = 6.67.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (Tc).  Typical Value = 1.
	 */
	public Seconds tc;
	/**
	 * Potential circuit phase angle (thetap).  Typical Value = 20.
	 */
	public AngleDegrees thetap;
	/**
	 * Forward time constant of inner loop field regulator (Tm).  Typical Value = 1.
	 */
	public Seconds tm;
	/**
	 * Maximum excitation voltage (Vbmax).  Typical Value = 8.63.
	 */
	public PU vbmax;
	/**
	 * Maximum inner loop feedback voltage (Vgmax).  Typical Value = 6.53.
	 */
	public PU vgmax;
	/**
	 * Maximum voltage regulator input limit (Vimax).  Typical Value = 0.2.
	 */
	public PU vimax;
	/**
	 * Minimum voltage regulator input limit (Vimin).  Typical Value = -0.2.
	 */
	public PU vimin;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = 0.
	 */
	public PU vrmin;
	/**
	 * Reactance associated with potential source (Xl).  Typical Value = 0.09.
	 */
	public PU xl;

	public ExcST3A(){

	}
}//end ExcST3A