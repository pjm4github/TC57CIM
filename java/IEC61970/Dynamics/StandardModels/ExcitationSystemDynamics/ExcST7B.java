package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE ST7B static excitation system without stator current limiter
 * (SCL) and current compensator (DROOP) inputs.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcST7B extends ExcitationSystemDynamics {

	/**
	 * High-value gate feedback gain (Kh).  Typical Value = 1.
	 */
	public PU kh;
	/**
	 * Voltage regulator integral gain (Kia).  Typical Value = 1.
	 */
	public PU kia;
	/**
	 * Low-value gate feedback gain (Kl).  Typical Value = 1.
	 */
	public PU kl;
	/**
	 * Voltage regulator proportional gain (Kpa).  Typical Value = 40.
	 */
	public PU kpa;
	/**
	 * OEL input selector (OELin). Typical Value = noOELinput.
	 */
	public ExcST7BOELselectorKind oelin;
	/**
	 * Regulator lag time constant (Tb).  Typical Value = 1.
	 */
	public Seconds tb;
	/**
	 * Regulator lead time constant (Tc).  Typical Value = 1.
	 */
	public Seconds tc;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
	 */
	public Seconds tf;
	/**
	 * Feedback time constant of inner loop field voltage regulator (Tg).  Typical
	 * Value = 1.
	 */
	public Seconds tg;
	/**
	 * Feedback time constant (Tia).  Typical Value = 3.
	 */
	public Seconds tia;
	/**
	 * Rectifier firing time constant (Ts).  Typical Value = 0.
	 */
	public Seconds ts;
	/**
	 * UEL input selector (UELin). Typical Value = noUELinput.
	 */
	public ExcST7BUELselectorKind uelin;
	/**
	 * Maximum voltage reference signal (Vmax).  Typical Value = 1.1.
	 */
	public PU vmax;
	/**
	 * Minimum voltage reference signal (Vmin).  Typical Value = 0.9.
	 */
	public PU vmin;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 5.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = -4.5.
	 */
	public PU vrmin;

	public ExcST7B(){

	}
}//end ExcST7B