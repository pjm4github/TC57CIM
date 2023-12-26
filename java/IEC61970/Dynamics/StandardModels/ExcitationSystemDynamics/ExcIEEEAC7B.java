package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type AC7B model. The model represents
 * excitation systems which consist of an ac alternator with either stationary or
 * rotating rectifiers to produce the dc field requirements. It is an upgrade to
 * earlier ac excitation systems, which replace only the controls but retain the
 * ac alternator and diode rectifier bridge.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 6.7.
 * 
 * <b>Note: </b>In the IEEE Standard 421.5 - 2005, the [1 / sT<sub>E</sub>] block
 * is shown as [1 / (1 + sT<sub>E</sub>)], which is incorrect.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEAC7B extends ExcitationSystemDynamics {

	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 0.18.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances
	 * (K<sub>D</sub>).  Typical Value = 0.02.
	 */
	public PU kd;
	/**
	 * Voltage regulator derivative gain (K<sub>DR</sub>).  Typical Value = 0.
	 */
	public PU kdr;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gain (K<sub>F1</sub>).  Typical Value = 0.
	 * 212.
	 */
	public PU kf1;
	/**
	 * Excitation control system stabilizer gain (K<sub>F2</sub>).  Typical Value = 0.
	 */
	public PU kf2;
	/**
	 * Excitation control system stabilizer gain (K<sub>F3</sub>).  Typical Value = 0.
	 */
	public PU kf3;
	/**
	 * Voltage regulator integral gain (K<sub>IA</sub>).  Typical Value = 59.69.
	 */
	public PU kia;
	/**
	 * Voltage regulator integral gain (K<sub>IR</sub>).  Typical Value = 4.24.
	 */
	public PU kir;
	/**
	 * Exciter field voltage lower limit parameter (K<sub>L</sub>).  Typical Value =
	 * 10.
	 */
	public PU kl;
	/**
	 * Potential circuit gain coefficient (K<sub>P</sub>).  Typical Value = 4.96.
	 */
	public PU kp;
	/**
	 * Voltage regulator proportional gain (K<sub>PA</sub>).  Typical Value = 65.36.
	 */
	public PU kpa;
	/**
	 * Voltage regulator proportional gain (K<sub>PR</sub>).  Typical Value = 4.24.
	 */
	public PU kpr;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
	 * Typical Value = 0.44.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
	 * Typical Value = 0.075.
	 */
	public Float seve2;
	/**
	 * Lag time constant (T<sub>DR</sub>).  Typical Value = 0.
	 */
	public Seconds tdr;
	/**
	 * Exciter time constant, integration rate associated with exciter control
	 * (T<sub>E</sub>).  Typical Value = 1.1.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
	 * Value = 1.
	 */
	public Seconds tf;
	/**
	 * Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 1.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -0.95.
	 */
	public PU vamin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (V<sub>E1</sub>) equals V<sub>EMAX</sub> (V<sub>E1</sub>).
	 *  Typical Value = 6.3.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (V<sub>E2</sub>).  Typical Value = 3.02.
	 */
	public PU ve2;
	/**
	 * Minimum exciter voltage output (V<sub>EMIN</sub>).  Typical Value = 0.
	 */
	public PU vemin;
	/**
	 * Exciter field current limit reference (V<sub>FEMAX</sub>).  Typical Value = 6.9.
	 */
	public PU vfemax;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 5.79.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -5.79.
	 */
	public PU vrmin;

	public ExcIEEEAC7B(){

	}
}//end ExcIEEEAC7B