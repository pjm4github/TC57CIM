package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * General Purpose Rotating Excitation System Model.  This model can be used to
 * represent a wide range of excitation systems whose DC power source is an AC or
 * DC generator. It encompasses IEEE type AC1, AC2, DC1, and DC2 excitation system
 * models.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcREXS extends ExcitationSystemDynamics {

	/**
	 * Field voltage value 1 (E1).  Typical Value = 3.
	 */
	public PU e1;
	/**
	 * Field voltage value 2 (E2).  Typical Value = 4.
	 */
	public PU e2;
	/**
	 * Rate feedback signal flag (Fbf). Typical Value = fieldCurrent.
	 */
	public ExcREXSFeedbackSignalKind fbf;
	/**
	 * Limit type flag (Flimf).  Typical Value = 0.
	 */
	public PU flimf;
	/**
	 * Rectifier regulation factor (Kc).  Typical Value = 0.05.
	 */
	public PU kc;
	/**
	 * Exciter regulation factor (Kd).  Typical Value = 2.
	 */
	public PU kd;
	/**
	 * Exciter field proportional constant (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Field voltage feedback gain (Kefd).  Typical Value = 0.
	 */
	public PU kefd;
	/**
	 * Rate feedback gain (Kf).  Typical Value = 0.05.
	 */
	public Seconds kf;
	/**
	 * Field voltage controller feedback gain (Kh).  Typical Value = 0.
	 */
	public PU kh;
	/**
	 * Field Current Regulator Integral Gain (Kii).  Typical Value = 0.
	 */
	public PU kii;
	/**
	 * Field Current Regulator Proportional Gain (Kip).  Typical Value = 1.
	 */
	public PU kip;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Voltage Regulator Integral Gain (Kvi).  Typical Value = 0.
	 */
	public PU kvi;
	/**
	 * Voltage Regulator Proportional Gain (Kvp).  Typical Value = 2800.
	 */
	public PU kvp;
	/**
	 * V/Hz limiter gain (Kvphz).  Typical Value = 0.
	 */
	public PU kvphz;
	/**
	 * Pickup speed of V/Hz limiter (Nvphz).  Typical Value = 0.
	 */
	public PU nvphz;
	/**
	 * Saturation factor at E1 (Se1).  Typical Value = 0.0001.
	 */
	public PU se1;
	/**
	 * Saturation factor at E2 (Se2).  Typical Value = 0.001.
	 */
	public PU se2;
	/**
	 * Voltage Regulator time constant (Ta).  Typical Value = 0.01.
	 */
	public Seconds ta;
	/**
	 * Lag time constant (Tb1).  Typical Value = 0.
	 */
	public Seconds tb1;
	/**
	 * Lag time constant (Tb2).  Typical Value = 0.
	 */
	public Seconds tb2;
	/**
	 * Lead time constant (Tc1).  Typical Value = 0.
	 */
	public Seconds tc1;
	/**
	 * Lead time constant (Tc2).  Typical Value = 0.
	 */
	public Seconds tc2;
	/**
	 * Exciter field time constant (Te).  Typical Value = 1.2.
	 */
	public Seconds te;
	/**
	 * Rate feedback time constant (Tf).  Typical Value = 1.
	 */
	public Seconds tf;
	/**
	 * Feedback lead time constant (Tf1).  Typical Value = 0.
	 */
	public Seconds tf1;
	/**
	 * Feedback lag time constant (Tf2).  Typical Value = 0.
	 */
	public Seconds tf2;
	/**
	 * Field current Bridge time constant (Tp).  Typical Value = 0.
	 */
	public Seconds tp;
	/**
	 * Maximum compounding voltage (Vcmax).  Typical Value = 0.
	 */
	public PU vcmax;
	/**
	 * Maximum Exciter Field Current (Vfmax).  Typical Value = 47.
	 */
	public PU vfmax;
	/**
	 * Minimum Exciter Field Current (Vfmin).  Typical Value = -20.
	 */
	public PU vfmin;
	/**
	 * Voltage Regulator Input Limit (Vimax).  Typical Value = 0.1.
	 */
	public PU vimax;
	/**
	 * Maximum controller output (Vrmax).  Typical Value = 47.
	 */
	public PU vrmax;
	/**
	 * Minimum controller output (Vrmin).  Typical Value = -20.
	 */
	public PU vrmin;
	/**
	 * Exciter compounding reactance (Xc).  Typical Value = 0.
	 */
	public PU xc;

	public ExcREXS(){

	}
}//end ExcREXS