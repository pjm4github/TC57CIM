package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.AngleDegrees;

/**
 * The class represents IEEE Std 421.5-2005 type ST4B model. This model is a
 * variation of the Type ST3A model, with a proportional plus integral (PI)
 * regulator block replacing the lag-lead regulator characteristic that is in the
 * ST3A model. Both potential and compound source rectifier excitation systems are
 * modeled.  The PI regulator blocks have non-windup limits that are represented.
 * The voltage regulator of this model is typically implemented digitally.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 7.4.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEST4B extends ExcitationSystemDynamics {

	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 0.113.
	 */
	public PU kc;
	/**
	 * Feedback gain constant of the inner loop field regulator (K<sub>G</sub>).
	 * Typical Value = 0.
	 */
	public PU kg;
	/**
	 * Potential circuit gain coefficient (K<sub>I</sub>).  Typical Value = 0.
	 */
	public PU ki;
	/**
	 * Voltage regulator integral gain output (K<sub>IM</sub>).  Typical Value = 0.
	 */
	public PU kim;
	/**
	 * Voltage regulator integral gain (K<sub>IR</sub>).  Typical Value = 10.75.
	 */
	public PU kir;
	/**
	 * Potential circuit gain coefficient (K<sub>P</sub>).  Typical Value = 9.3.
	 */
	public PU kp;
	/**
	 * Voltage regulator proportional gain output (K<sub>PM</sub>).  Typical Value = 1.
	 */
	public PU kpm;
	/**
	 * Voltage regulator proportional gain (K<sub>PR</sub>).  Typical Value = 10.75.
	 */
	public PU kpr;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.02.
	 */
	public Seconds ta;
	/**
	 * Potential circuit phase angle (thetap).  Typical Value = 0.
	 */
	public AngleDegrees thetap;
	/**
	 * Maximum excitation voltage (V<sub>BMax</sub>).  Typical Value = 11.63.
	 */
	public PU vbmax;
	/**
	 * Maximum inner loop output (V<sub>MMax</sub>).  Typical Value = 99.
	 */
	public PU vmmax;
	/**
	 * Minimum inner loop output (V<sub>MMin</sub>).  Typical Value = -99.
	 */
	public PU vmmin;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -0.87.
	 */
	public PU vrmin;
	/**
	 * Reactance associated with potential source (X<sub>L</sub>).  Typical Value = 0.
	 * 124.
	 */
	public PU xl;

	public ExcIEEEST4B(){

	}
}//end ExcIEEEST4B