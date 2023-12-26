package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE ST6B static excitation system with PID controller and optional
 * inner feedbacks loop.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcST6B extends ExcitationSystemDynamics {

	/**
	 * Exciter output current limit reference (Ilr).  Typical Value = 4.164.
	 */
	public PU ilr;
	/**
	 * Selector (K1).
	 * true = feedback is from Ifd
	 * false = feedback is not from Ifd.
	 * Typical Value = true.
	 */
	public Boolean k1;
	/**
	 * Exciter output current limit adjustment (Kcl).  Typical Value = 1.0577.
	 */
	public PU kcl;
	/**
	 * Pre-control gain constant of the inner loop field regulator (Kff).  Typical
	 * Value = 1.
	 */
	public PU kff;
	/**
	 * Feedback gain constant of the inner loop field regulator (Kg).  Typical Value =
	 * 1.
	 */
	public PU kg;
	/**
	 * Voltage regulator integral gain (Kia).  Typical Value = 45.094.
	 */
	public PU kia;
	/**
	 * Exciter output current limit adjustment (Kcl).  Typical Value = 17.33.
	 */
	public PU klr;
	/**
	 * Forward gain constant of the inner loop field regulator (Km).  Typical Value =
	 * 1.
	 */
	public PU km;
	/**
	 * Voltage regulator proportional gain (Kpa).  Typical Value = 18.038.
	 */
	public PU kpa;
	/**
	 * Voltage regulator derivative gain (Kvd).  Typical Value = 0.
	 */
	public PU kvd;
	/**
	 * OEL input selector (OELin). Typical Value = noOELinput.
	 */
	public ExcST6BOELselectorKind oelin;
	/**
	 * Feedback time constant of inner loop field voltage regulator (Tg).  Typical
	 * Value = 0.02.
	 */
	public Seconds tg;
	/**
	 * Rectifier firing time constant (Ts).  Typical Value = 0.
	 */
	public Seconds ts;
	/**
	 * Voltage regulator derivative gain (Tvd).  Typical Value = 0.
	 */
	public Seconds tvd;
	/**
	 * Maximum voltage regulator output (Vamax).  Typical Value = 4.81.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (Vamin).  Typical Value = -3.85.
	 */
	public PU vamin;
	/**
	 * Selector (Vilim).
	 * true = Vimin-Vimax limiter is active
	 * false = Vimin-Vimax limiter is not active.
	 * Typical Value = true.
	 */
	public Boolean vilim;
	/**
	 * Maximum voltage regulator input limit (Vimax).  Typical Value = 10.
	 */
	public PU vimax;
	/**
	 * Minimum voltage regulator input limit (Vimin).  Typical Value = -10.
	 */
	public PU vimin;
	/**
	 * Selector (Vmult).
	 * true = multiply regulator output by terminal voltage
	 * false = do not multiply regulator output by terminal voltage.
	 * Typical Value = true.
	 */
	public Boolean vmult;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 4.81.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = -3.85.
	 */
	public PU vrmin;
	/**
	 * Excitation source reactance (Xc).  Typical Value = 0.05.
	 */
	public PU xc;

	public ExcST6B(){

	}
}//end ExcST6B