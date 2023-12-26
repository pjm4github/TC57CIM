package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE AC1A alternator-supplied rectifier excitation system with
 * different rate feedback source.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAC1A extends ExcitationSystemDynamics {

	/**
	 * Indicates if both HV gate and LV gate are active (HVLVgates).
	 * true = gates are used
	 * false = gates are not used.
	 * Typical Value = true.
	 */
	public Boolean hvlvgates;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 400.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc). Typical
	 * Value = 0.2.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances (Kd).
	 * Typical Value = 0.38.
	 */
	public PU kd;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (Kf).  Typical Value = 0.03.
	 */
	public PU kf;
	/**
	 * Coefficient to allow different usage of the model (Kf1).  Typical Value = 0.
	 */
	public PU kf1;
	/**
	 * Coefficient to allow different usage of the model (Kf2).  Typical Value = 1.
	 */
	public PU kf2;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Ve1,
	 * back of commutating reactance (Se[Ve1]).  Typical Value = 0.1.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Ve2,
	 * back of commutating reactance (Se[Ve2]).  Typical Value = 0.03.
	 */
	public Float seve2;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.02.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (Tb).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (T<sub>c</sub>).  Typical Value = 0.
	 */
	public Seconds tc;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 * Typical Value = 0.8.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
	 */
	public Seconds tf;
	/**
	 * Maximum voltage regulator output (V<sub>amax</sub>).  Typical Value = 14.5.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>amin</sub>).  Typical Value = -14.5.
	 */
	public PU vamin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve1).  Typical Value = 4.18.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve2).  Typical Value = 3.14.
	 */
	public PU ve2;
	/**
	 * Maximum voltage regulator outputs (Vrmax).  Typical Value = 6.03.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator outputs (Rrmin).  Typical Value = -5.43.
	 */
	public PU vrmin;

	public ExcAC1A(){

	}
}//end ExcAC1A