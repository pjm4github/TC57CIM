package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type ST7B model. This model is
 * representative of static potential-source excitation systems. In this system,
 * the AVR consists of a PI voltage regulator. A phase lead-lag filter in series
 * allows introduction of a derivative function, typically used with brushless
 * excitation systems. In that case, the regulator is of the PID type. In addition,
 * the terminal voltage channel includes a phase lead-lag filter.  The AVR
 * includes the appropriate inputs on its reference for overexcitation limiter
 * (OEL1), underexcitation limiter (UEL), stator current limiter (SCL), and
 * current compensator (DROOP). All these limitations, when they work at voltage
 * reference level, keep the PSS (VS signal from Type PSS1A, PSS2A, or PSS2B) in
 * operation. However, the UEL limitation can also be transferred to the high
 * value (HV) gate acting on the output signal. In addition, the output signal
 * passes through a low value (LV) gate for a ceiling overexcitation limiter
 * (OEL2).
 * 
 * Reference: IEEE Standard 421.5-2005 Section 7.7.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEST7B extends ExcitationSystemDynamics {

	/**
	 * High-value gate feedback gain (K<sub>H</sub>).  Typical Value 1.
	 */
	public PU kh;
	/**
	 * Voltage regulator integral gain (K<sub>IA</sub>).  Typical Value = 1.
	 */
	public PU kia;
	/**
	 * Low-value gate feedback gain (K<sub>L</sub>).  Typical Value 1.
	 */
	public PU kl;
	/**
	 * Voltage regulator proportional gain (K<sub>PA</sub>).  Typical Value = 40.
	 */
	public PU kpa;
	/**
	 * OEL input selector (OELin). Typical Value = noOELinput.
	 */
	public ExcST7BOELselectorKind oelin;
	/**
	 * Regulator lag time constant (T<sub>B</sub>).  Typical Value 1.
	 */
	public Seconds tb;
	/**
	 * Regulator lead time constant (T<sub>C</sub>).  Typical Value 1.
	 */
	public Seconds tc;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
	 * Value 1.
	 */
	public Seconds tf;
	/**
	 * Feedback time constant of inner loop field voltage regulator (T<sub>G</sub>).
	 * Typical Value 1.
	 */
	public Seconds tg;
	/**
	 * Feedback time constant (T<sub>IA</sub>).  Typical Value = 3.
	 */
	public Seconds tia;
	/**
	 * UEL input selector (UELin). Typical Value = noUELinput.
	 */
	public ExcST7BUELselectorKind uelin;
	/**
	 * Maximum voltage reference signal (V<sub>MAX</sub>).  Typical Value = 1.1.
	 */
	public PU vmax;
	/**
	 * Minimum voltage reference signal (V<sub>MIN</sub>).  Typical Value = 0.9.
	 */
	public PU vmin;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 5.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -4.5.
	 */
	public PU vrmin;

	public ExcIEEEST7B(){

	}
}//end ExcIEEEST7B