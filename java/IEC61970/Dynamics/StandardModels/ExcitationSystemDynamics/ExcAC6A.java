package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE AC6A alternator-supplied rectifier excitation system with speed
 * input.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAC6A extends ExcitationSystemDynamics {

	/**
	 * Voltage regulator gain (Ka).  Typical Value = 536.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc).  Typical
	 * Value = 0.173.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances (Kd).
	 * Typical Value = 1.91.
	 */
	public PU kd;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.6.
	 */
	public PU ke;
	/**
	 * Exciter field current limiter gain (Kh).  Typical Value = 92.
	 */
	public PU kh;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Ve1,
	 * back of commutating reactance (Se[Ve1]).  Typical Value = 0.214.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Ve2,
	 * back of commutating reactance (Se[Ve2]).  Typical Value = 0.044.
	 */
	public Float seve2;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.086.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (Tb).  Typical Value = 9.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (Tc).  Typical Value = 3.
	 */
	public Seconds tc;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 * Typical Value = 1.
	 */
	public Seconds te;
	/**
	 * Exciter field current limiter time constant (Th).  Typical Value = 0.08.
	 */
	public Seconds th;
	/**
	 * Exciter field current limiter time constant (Tj).  Typical Value = 0.02.
	 */
	public Seconds tj;
	/**
	 * Voltage regulator time constant (Tk).  Typical Value = 0.18.
	 */
	public Seconds tk;
	/**
	 * Maximum voltage regulator output (Vamax).  Typical Value = 75.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (Vamin).  Typical Value = -75.
	 */
	public PU vamin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve<sub>1</sub>).  Typical Value = 7.4.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve2).  Typical Value = 5.55.
	 */
	public PU ve2;
	/**
	 * Exciter field current limit reference (Vfelim).  Typical Value = 19.
	 */
	public PU vfelim;
	/**
	 * Maximum field current limiter signal reference (Vhmax).  Typical Value = 75.
	 */
	public PU vhmax;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 44.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = -36.
	 */
	public PU vrmin;

	public ExcAC6A(){

	}
}//end ExcAC6A