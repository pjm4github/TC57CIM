package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type AC1A model. The model represents
 * the field-controlled alternator-rectifier excitation systems designated Type
 * AC1A. These excitation systems consist of an alternator main exciter with non-
 * controlled rectifiers.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 6.1.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEAC1A extends ExcitationSystemDynamics {

	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 400.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (K<sub>C</sub>).
	 * Typical Value = 0.2.
	 */
	public PU kc;
	/**
	 * Demagnetizing factor, a function of exciter alternator reactances
	 * (K<sub>D</sub>).  Typical Value = 0.38.
	 */
	public PU kd;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (K<sub>F</sub>).  Typical Value = 0.
	 * 03.
	 */
	public PU kf;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E1</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E1</sub>]).
	 * Typical Value = 0.1.
	 */
	public Float seve1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * V<sub>E2</sub>, back of commutating reactance (S<sub>E</sub>[V<sub>E2</sub>]).
	 * Typical Value = 0.03.
	 */
	public Float seve2;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.02.
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
	 * (T<sub>E</sub>).  Typical Value = 0.8.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
	 * Value = 1.
	 */
	public Seconds tf;
	/**
	 * Maximum voltage regulator output (V<sub>AMAX</sub>).  Typical Value = 14.5.
	 */
	public PU vamax;
	/**
	 * Minimum voltage regulator output (V<sub>AMIN</sub>).  Typical Value = -14.5.
	 */
	public PU vamin;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (V<sub>E1</sub>).  Typical Value = 4.18.
	 */
	public PU ve1;
	/**
	 * Exciter alternator output voltages back of commutating reactance at which
	 * saturation is defined (V<sub>E2</sub>).  Typical Value = 3.14.
	 */
	public PU ve2;
	/**
	 * Maximum voltage regulator outputs (V<sub>RMAX</sub>).  Typical Value = 6.03.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator outputs (V<sub>RMIN</sub>).  Typical Value = -5.43.
	 */
	public PU vrmin;

	public ExcIEEEAC1A(){

	}
}//end ExcIEEEAC1A