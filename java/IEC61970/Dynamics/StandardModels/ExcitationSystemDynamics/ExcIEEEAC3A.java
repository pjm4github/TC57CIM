package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type AC3A model. The model represents
 * the field-controlled alternator-rectifier excitation systems designated Type
 * AC3A. These excitation systems include an alternator main exciter with non-
 * controlled rectifiers. The exciter employs self-excitation, and the voltage
 * regulator power is derived from the exciter output voltage.  Therefore, this
 * system has an additional nonlinearity, simulated by the use of a multiplier
 * whose inputs are the voltage regulator command signal, <b>Va</b>, and the
 * exciter output voltage, <b>Efd</b>, times <b>K</b><b><sub>R</sub></b>.  This
 * model is applicable to excitation systems employing static voltage regulators.
 * 
 * 
 * Reference: IEEE Standard 421.5-2005 Section 6.3.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEAC3A extends ExcitationSystemDynamics {

	/**
	 * Value of <i>EFD </i>at which feedback gain changes (E<sub>FDN</sub>).  Typical
	 * Value = 2.36.
	 */
	public PU efdn;
	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 45.62.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 0.104.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances
	 * (K<sub>D</sub>).  Typical Value = 0.499.
	 */
	public PU kd;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
	 * 143.
	 */
	public PU kf;
	/**
	 * Excitation control system stabilizer gain (K<sub>N</sub>).  Typical Value = 0.
	 * 05.
	 */
	public PU kn;
	/**
	 * Constant associated with regulator and alternator field power supply
	 * (K<sub>R</sub>).  Typical Value = 3.77.
	 */
	public PU kr;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
	 * Typical Value = 1.143.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
	 * Typical Value = 0.1.
	 */
	public Float seve2;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.013.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (T<sub>B</sub>).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (T<sub>C</sub>).  Typical Value = 0.
	 */
	public Seconds tc;
	/**
	 * Exciter time constant, integration rate associated with exciter control
	 * (T<sub>E</sub>).  Typical Value = 1.17.
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
	 * saturation is defined (V<sub>E1</sub>) equals V<sub>EMAX </sub>(V<sub>E1</sub>).
	 *  Typical Value = 6.24.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (V<sub>E2</sub>).  Typical Value = 4.68.
	 */
	public PU ve2;
	/**
	 * Minimum exciter voltage output (V<sub>EMIN</sub>).  Typical Value = 0.1.
	 */
	public PU vemin;
	/**
	 * Exciter field current limit reference (V<sub>FEMAX</sub>).  Typical Value = 16.
	 */
	public PU vfemax;

	public ExcIEEEAC3A(){

	}
}//end ExcIEEEAC3A