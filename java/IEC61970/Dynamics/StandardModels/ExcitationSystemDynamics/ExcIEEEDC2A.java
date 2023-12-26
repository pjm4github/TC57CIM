package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;

/**
 * The class represents IEEE Std 421.5-2005 type DC2A model. This model represents
 * represent field-controlled dc commutator exciters with continuously acting
 * voltage regulators having supplies obtained from the generator or auxiliary bus.
 *  It differs from the Type DC1A model only in the voltage regulator output
 * limits, which are now proportional to terminal voltage
 * <b>V</b><b><sub>T</sub></b>.
 * It is representative of solid-state replacements for various forms of older
 * mechanical and rotating amplifier regulating equipment connected to dc
 * commutator exciters.
 * 
 * Reference: IEEE Standard 421.5-2005 Section 5.2.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEDC2A extends ExcitationSystemDynamics {

	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
	 * Typical Value = 3.05.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
	 * Typical Value = 2.29.
	 */
	public PU efd2;
	/**
	 * (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
	 * Typical Value = - 999  which means that there is no limit applied.
	 */
	public PU exclim;
	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 300.
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gain (K<sub>F</sub>).  Typical Value = 0.1.
	 */
	public PU kf;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.279.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.117.
	 */
	public Float seefd2;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.01.
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
	 * (T<sub>E</sub>).  Typical Value = 1.33.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
	 * Value = 0.675.
	 */
	public Seconds tf;
	/**
	 * UEL input (uelin).
	 * true = input is connected to the HV gate
	 * false = input connects to the error signal.
	 * Typical Value = true.
	 */
	public Boolean uelin;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 4.95.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -4.9.
	 */
	public PU vrmin;

	public ExcIEEEDC2A(){

	}
}//end ExcIEEEDC2A