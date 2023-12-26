package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE AC8B alternator-supplied rectifier excitation system with speed
 * input and input limiter.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAC8B extends ExcitationSystemDynamics {

	/**
	 * Input limiter indicator.
	 * true = input limiter Vimax and Vimin is considered
	 * false = input limiter Vimax and Vimin is not considered.
	 * Typical Value = true.
	 */
	public Boolean inlim;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 1.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc). Typical
	 * Value = 0.55.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances (Kd).
	 * Typical Value = 1.1.
	 */
	public PU kd;
	/**
	 * Voltage regulator derivative gain (Kdr).  Typical Value = 10.
	 */
	public PU kdr;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Voltage regulator integral gain (Kir).  Typical Value = 5.
	 */
	public PU kir;
	/**
	 * Voltage regulator proportional gain (Kpr).  Typical Value = 80.
	 */
	public PU kpr;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * PID limiter indicator.
	 * true = input limiter Vpidmax and Vpidmin is considered
	 * false = input limiter Vpidmax and Vpidmin is not considered.
	 * Typical Value = true.
	 */
	public Boolean pidlim;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * Ve<sub>1</sub>, back of commutating reactance (Se[Ve1]).  Typical Value = 0.3.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * Ve<sub>2</sub>, back of commutating reactance (Se[Ve2]).  Typical Value = 3.
	 */
	public Float seve2;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.
	 */
	public Seconds ta;
	/**
	 * Lag time constant (Tdr).  Typical Value = 0.1.
	 */
	public Seconds tdr;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 * Typical Value = 1.2.
	 */
	public Seconds te;
	/**
	 * Selector for the limiter on the block [1/sTe].
	 * See diagram for meaning of true and false.
	 * Typical Value = false.
	 */
	public Boolean telim;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve<sub>1</sub>) equals V<sub>EMAX</sub> (Ve1).  Typical
	 * Value = 6.5.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (Ve<sub>2</sub>).  Typical Value = 9.
	 */
	public PU ve2;
	/**
	 * Minimum exciter voltage output (Vemin).  Typical Value = 0.
	 */
	public PU vemin;
	/**
	 * Exciter field current limit reference (Vfemax).  Typical Value = 6.
	 */
	public PU vfemax;
	/**
	 * Input signal maximum (Vimax).  Typical Value = 35.
	 */
	public PU vimax;
	/**
	 * Input signal minimum (Vimin).  Typical Value = -10.
	 */
	public PU vimin;
	/**
	 * PID maximum controller output (Vpidmax).  Typical Value = 35.
	 */
	public PU vpidmax;
	/**
	 * PID minimum controller output (Vpidmin).  Typical Value = -10.
	 */
	public PU vpidmin;
	/**
	 * Maximum voltage regulator output (Vrmax). Typical Value = 35.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = 0.
	 */
	public PU vrmin;
	/**
	 * Multiply by generator's terminal voltage indicator.
	 * true =the limits Vrmax and Vrmin are multiplied by the generator's terminal
	 * voltage to represent a thyristor power stage fed from the generator terminals
	 * false = limits are not multiplied by generator's terminal voltage.
	 * Typical Value = false.
	 */
	public Boolean vtmult;

	public ExcAC8B(){

	}
}//end ExcAC8B