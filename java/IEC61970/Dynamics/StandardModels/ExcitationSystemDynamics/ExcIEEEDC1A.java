package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type DC1A model. This model represents
 * field-controlled dc commutator exciters with continuously acting voltage
 * regulators (especially the direct-acting rheostatic, rotating amplifier, and
 * magnetic amplifier types).  Because this model has been widely implemented by
 * the industry, it is sometimes used to represent other types of systems when
 * detailed data for them are not available or when a simplified model is required.
 * 
 * 
 * 
 * Reference: IEEE Standard 421.5-2005 Section 5.1.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEDC1A extends ExcitationSystemDynamics {

	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
	 * Typical Value = 3.1.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
	 * Typical Value = 2.3.
	 */
	public PU efd2;
	/**
	 * (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
	 * true = a lower limit of zero is applied to integrator output
	 * false = a lower limit of zero is not applied to integrator output.
	 * Typical Value = true.
	 */
	public Boolean exclim;
	/**
	 * Voltage regulator gain (K<sub>A</sub>).  Typical Value = 46.
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 0.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gain (K<sub>F</sub>).  Typical Value = 0.1.
	 */
	public PU kf;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.33.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.1.
	 */
	public Float seefd2;
	/**
	 * Voltage regulator time constant (T<sub>A</sub>).  Typical Value = 0.06.
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
	 * (T<sub>E</sub>).  Typical Value = 0.46.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (T<sub>F</sub>).  Typical
	 * Value = 1.
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
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = -0.9.
	 */
	public PU vrmin;

	public ExcIEEEDC1A(){

	}
}//end ExcIEEEDC1A