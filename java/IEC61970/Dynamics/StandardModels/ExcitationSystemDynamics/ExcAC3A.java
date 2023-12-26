package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Float;

/**
 * Modified IEEE AC3A alternator-supplied rectifier excitation system with
 * different field current limit.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAC3A extends ExcitationSystemDynamics {

	/**
	 * Value of <i>EFD </i>at which feedback gain changes (Efdn).  Typical Value = 2.
	 * 36.
	 */
	public PU efdn;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 45.62.
	 */
	public Seconds ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc).  Typical
	 * Value = 0.104.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances (Kd).
	 * Typical Value = 0.499.
	 */
	public PU kd;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (Kf).  Typical Value = 0.143.
	 */
	public PU kf;
	/**
	 * Coefficient to allow different usage of the model (Kf1).  Typical Value = 1.
	 */
	public PU kf1;
	/**
	 * Coefficient to allow different usage of the model (Kf2).  Typical Value = 0.
	 */
	public PU kf2;
	/**
	 * Gain used in the minimum field voltage limiter loop (Klv).  Typical Value = 0.
	 * 194.
	 */
	public PU klv;
	/**
	 * Excitation control system stabilizer gain (Kn).  Typical Value =0.05.
	 */
	public PU kn;
	/**
	 * Constant associated with regulator and alternator field power supply (Kr).
	 * Typical Value =3.77.
	 */
	public PU kr;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]).  Typical
	 * Value = 1.143.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]).  Typical
	 * Value = 0.1.
	 */
	public Float seve2;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.013.
	 */
	public PU ta;
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
	 * Typical Value = 1.17.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
	 */
	public Seconds tf;
	/**
	 * Maximum voltage regulator output (V<sub>amax</sub>).  Typical Value = 1.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>amin</sub>).  Typical Value = -0.95.
	 */
	public PU vamin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve1) equals Vemax (Ve1).  Typical Value = 6.24.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve<sub>2</sub>).  Typical Value = 4.68.
	 */
	public PU ve2;
	/**
	 * Minimum exciter voltage output (Vemin).  Typical Value = 0.1.
	 */
	public PU vemin;
	/**
	 * Exciter field current limit reference (Vfemax).  Typical Value = 16.
	 */
	public PU vfemax;
	/**
	 * Field voltage used in the minimum field voltage limiter loop (Vlv).  Typical
	 * Value = 0.79.
	 */
	public PU vlv;

	public ExcAC3A(){

	}
}//end ExcAC3A