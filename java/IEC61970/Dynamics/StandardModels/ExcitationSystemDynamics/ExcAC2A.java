package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE AC2A alternator-supplied rectifier excitation system with
 * different field current limit.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAC2A extends ExcitationSystemDynamics {

	/**
	 * Indicates if HV gate is active (HVgate).
	 * true = gate is used
	 * false = gate is not used.
	 * Typical Value = true.
	 */
	public Boolean hvgate;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 400.
	 */
	public PU ka;
	/**
	 * Second stage regulator gain (Kb) (>0).  Exciter field current controller gain.
	 * Typical Value = 25.
	 */
	public PU kb;
	/**
	 * Second stage regulator gain (Kb1). It is exciter field current controller gain
	 * used as alternative to Kb to represent a variant of the ExcAC2A model.  Typical
	 * Value = 25.
	 */
	public PU kb1;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc).  Typical
	 * Value = 0.28.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances (Kd).
	 * Typical Value = 0.35.
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
	 * Exciter field current feedback gain (Kh).  Typical Value = 1.
	 */
	public PU kh;
	/**
	 * Exciter field current limiter gain (Kl).  Typical Value = 10.
	 */
	public PU kl;
	/**
	 * Coefficient to allow different usage of the model (Kl1).  Typical Value = 1.
	 */
	public PU kl1;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Indicates if LV gate is active (LVgate).
	 * true = gate is used
	 * false = gate is not used.
	 * Typical Value = true.
	 */
	public Boolean lvgate;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * Ve<sub>1</sub>, back of commutating reactance (Se[Ve<sub>1</sub>]).  Typical
	 * Value = 0.037.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * Ve<sub>2</sub>, back of commutating reactance (Se[Ve<sub>2</sub>]).  Typical
	 * Value = 0.012.
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
	 * Typical Value = 0.6.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
	 */
	public Seconds tf;
	/**
	 * Maximum voltage regulator output (V<sub>amax</sub>).  Typical Value = 8.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>amin</sub>).  Typical Value = -8.
	 */
	public PU vamin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve<sub>1</sub>).  Typical Value = 4.4.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve<sub>2</sub>).  Typical Value = 3.3.
	 */
	public PU ve2;
	/**
	 * Exciter field current limit reference (Vfemax).  Typical Value = 4.4.
	 */
	public PU vfemax;
	/**
	 * Maximum exciter field current (Vlr).  Typical Value = 4.4.
	 */
	public PU vlr;
	/**
	 * Maximum voltage regulator outputs (Vrmax).  Typical Value = 105.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator outputs (Vrmin).  Typical Value = -95.
	 */
	public PU vrmin;

	public ExcAC2A(){

	}
}//end ExcAC2A