package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type AC6A model. The model represents
 * field-controlled alternator-rectifier excitation systems with system-supplied
 * electronic voltage regulators.  The maximum output of the regulator,
 * <b><i>V</i></b><b><i><sub>R</sub></i></b>, is a function of terminal voltage,
 * <b><i>V</i></b><b><i><sub>T</sub></i></b>. The field current limiter included
 * in the original model AC6A remains in the 2005 update.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 6.6.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEAC6A extends ExcitationSystemDynamics {

	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 536.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 0.173.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances
	 * (K<sub>D</sub>).  Typical Value = 1.91.
	 */
	public PU kd;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.6.
	 */
	public PU ke;
	/**
	 * Exciter field current limiter gain (K<sub>H</sub>).  Typical Value = 92.
	 */
	public PU kh;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
	 * Typical Value = 0.214.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
	 * Typical Value = 0.044.
	 */
	public Float seve2;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.086.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 9.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 3.
	 */
	public Seconds tc;
	/**
	 * Exciter time constant, integration rate associated with exciter control
	 * (T<sub>E</sub>).  Typical Value = 1.
	 */
	public Seconds te;
	/**
	 * Exciter field current limiter time constant (T<sub>H</sub>).  Typical Value = 0.
	 * 08.
	 */
	public Seconds th;
	/**
	 * Exciter field current limiter time constant (T<sub>J</sub>).  Typical Value = 0.
	 * 02.
	 */
	public Seconds tj;
	/**
	 * Voltage regulator time constant (T<sub>K</sub>).  Typical Value = 0.18.
	 */
	public Seconds tk;
	/**
	 * Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 75.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -75.
	 */
	public PU vamin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (V<sub>E1</sub>) equals V<sub>EMAX </sub>(V<sub>E1</sub>).
	 *  Typical Value = 7.4.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (V<sub>E2</sub>).  Typical Value = 5.55.
	 */
	public PU ve2;
	/**
	 * Exciter field current limit reference (V<sub>FELIM</sub>).  Typical Value = 19.
	 */
	public PU vfelim;
	/**
	 * Maximum field current limiter signal reference (V<sub>HMAX</sub>).  Typical
	 * Value = 75.
	 */
	public PU vhmax;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 44.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -36.
	 */
	public PU vrmin;

	public ExcIEEEAC6A(){

	}
}//end ExcIEEEAC6A