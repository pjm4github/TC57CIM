package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE PSS2B Model.  Extra lead/lag (or rate) block added at end (up to
 * 4 lead/lags total).
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class Pss2B extends PowerSystemStabilizerDynamics {

	/**
	 * Numerator constant (a).  Typical Value = 1.
	 */
	public Float a;
	/**
	 * Type of input signal #1.  Typical Value = rotorSpeed.
	 */
	public InputSignalKind inputSignal1Type;
	/**
	 * Type of input signal #2.  Typical Value = generatorElectricalPower.
	 */
	public InputSignalKind inputSignal2Type;
	/**
	 * Stabilizer gain (Ks1).  Typical Value = 12.
	 */
	public PU ks1;
	/**
	 * Gain on signal #2 (Ks2).  Typical Value = 0.2.
	 */
	public PU ks2;
	/**
	 * Gain on signal #2 input before ramp-tracking filter (Ks3).  Typical Value = 1.
	 */
	public PU ks3;
	/**
	 * Gain on signal #2 input after ramp-tracking filter (Ks4).  Typical Value = 1.
	 */
	public PU ks4;
	/**
	 * Denominator order of ramp tracking filter (M).  Typical Value = 5.
	 */
	public Integer m;
	/**
	 * Order of ramp tracking filter (N).  Typical Value = 1.
	 */
	public Integer n;
	/**
	 * Lead/lag time constant (T1).  Typical Value = 0.12.
	 */
	public Seconds t1;
	/**
	 * Lead/lag time constant (T10).  Typical Value = 0.
	 */
	public Seconds t10;
	/**
	 * Lead/lag time constant (T11).  Typical Value = 0.
	 */
	public Seconds t11;
	/**
	 * Lead/lag time constant (T2).  Typical Value = 0.02.
	 */
	public Seconds t2;
	/**
	 * Lead/lag time constant (T3).  Typical Value = 0.3.
	 */
	public Seconds t3;
	/**
	 * Lead/lag time constant (T4).  Typical Value = 0.02.
	 */
	public Seconds t4;
	/**
	 * Time constant on signal #1 (T6).  Typical Value = 0.
	 */
	public Seconds t6;
	/**
	 * Time constant on signal #2 (T7).  Typical Value = 2.
	 */
	public Seconds t7;
	/**
	 * Lead of ramp tracking filter (T8).  Typical Value = 0.2.
	 */
	public Seconds t8;
	/**
	 * Lag of ramp tracking filter (T9).  Typical Value = 0.1.
	 */
	public Seconds t9;
	/**
	 * Lead constant (Ta).  Typical Value = 0.
	 */
	public Seconds ta;
	/**
	 * Lag time constant (Tb).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * First washout on signal #1 (Tw1).  Typical Value = 2.
	 */
	public Seconds tw1;
	/**
	 * Second washout on signal #1 (Tw2).  Typical Value = 2.
	 */
	public Seconds tw2;
	/**
	 * First washout on signal #2 (Tw3).  Typical Value = 2.
	 */
	public Seconds tw3;
	/**
	 * Second washout on signal #2 (Tw4).  Typical Value = 0.
	 */
	public Seconds tw4;
	/**
	 * Input signal #1 max limit (Vsi1max).  Typical Value = 2.
	 */
	public PU vsi1max;
	/**
	 * Input signal #1 min limit (Vsi1min).  Typical Value = -2.
	 */
	public PU vsi1min;
	/**
	 * Input signal #2 max limit (Vsi2max).  Typical Value = 2.
	 */
	public PU vsi2max;
	/**
	 * Input signal #2 min limit (Vsi2min).  Typical Value = -2.
	 */
	public PU vsi2min;
	/**
	 * Stabilizer output max limit (Vstmax).  Typical Value = 0.1.
	 */
	public PU vstmax;
	/**
	 * Stabilizer output min limit (Vstmin).  Typical Value = -0.1.
	 */
	public PU vstmin;

	public Pss2B(){

	}
}//end Pss2B