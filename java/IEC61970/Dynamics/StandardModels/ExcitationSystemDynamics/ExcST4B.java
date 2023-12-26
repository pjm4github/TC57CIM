package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.AngleDegrees;

/**
 * Modified IEEE ST4B static excitation system with maximum inner loop feedback
 * gain <b>Vgmax</b>.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcST4B extends ExcitationSystemDynamics {

	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc). Typical
	 * Value = 0.113.
	 */
	public PU kc;
	/**
	 * Feedback gain constant of the inner loop field regulator (Kg). Typical Value =
	 * 0.
	 */
	public PU kg;
	/**
	 * Potential circuit gain coefficient (Ki).  Typical Value = 0.
	 */
	public PU ki;
	/**
	 * Voltage regulator integral gain output (Kim).  Typical Value = 0.
	 */
	public PU kim;
	/**
	 * Voltage regulator integral gain (Kir).  Typical Value = 10.75.
	 */
	public PU kir;
	/**
	 * Potential circuit gain coefficient (Kp).  Typical Value = 9.3.
	 */
	public PU kp;
	/**
	 * Voltage regulator proportional gain output (Kpm).  Typical Value = 1.
	 */
	public PU kpm;
	/**
	 * Voltage regulator proportional gain (Kpr).  Typical Value = 10.75.
	 */
	public PU kpr;
	/**
	 * Selector (LVgate).
	 * true = LVgate is part of the block diagram
	 * false = LVgate is not part of the block diagram.
	 * Typical Value = false.
	 */
	public Boolean lvgate;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.02.
	 */
	public Seconds ta;
	/**
	 * Potential circuit phase angle (thetap).  Typical Value = 0.
	 */
	public AngleDegrees thetap;
	/**
	 * Selector (Uel).
	 * true = UEL is part of block diagram
	 * false = UEL is not part of block diagram.
	 * Typical Value = false.
	 */
	public Boolean uel;
	/**
	 * Maximum excitation voltage (Vbmax).  Typical Value = 11.63.
	 */
	public PU vbmax;
	/**
	 * Maximum inner loop feedback voltage (Vgmax).  Typical Value = 5.8.
	 */
	public PU vgmax;
	/**
	 * Maximum inner loop output (Vmmax).  Typical Value = 99.
	 */
	public PU vmmax;
	/**
	 * Minimum inner loop output (Vmmin).  Typical Value = -99.
	 */
	public PU vmmin;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = -0.87.
	 */
	public PU vrmin;
	/**
	 * Reactance associated with potential source (Xl).  Typical Value = 0.124.
	 */
	public PU xl;

	public ExcST4B(){

	}
}//end ExcST4B