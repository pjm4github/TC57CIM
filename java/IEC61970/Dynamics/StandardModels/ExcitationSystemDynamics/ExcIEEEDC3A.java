package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * The class represents IEEE Std 421.5-2005 type DC3A model. This model represents
 * represent older systems, in particular those dc commutator exciters with non-
 * continuously acting regulators that were commonly used before the development
 * of the continuously acting varieties.  These systems respond at basically two
 * different rates, depending upon the magnitude of voltage error. For small
 * errors, adjustment is made periodically with a signal to a motor-operated
 * rheostat. Larger errors cause resistors to be quickly shorted or inserted and a
 * strong forcing signal applied to the exciter. Continuous motion of the motor-
 * operated rheostat occurs for these larger error signals, even though it is
 * bypassed by contactor action.
 * 
 * 
 * Reference: IEEE Standard 421.5-2005 Section 5.3.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcIEEEDC3A extends ExcitationSystemDynamics {

	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD1</sub>).
	 * Typical Value = 3.375.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (E<sub>FD2</sub>).
	 * Typical Value = 3.15.
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
	 * Exciter constant related to self-excited field (K<sub>E</sub>).  Typical Value
	 * = 0.05.
	 */
	public PU ke;
	/**
	 * Fast raise/lower contact setting (K<sub>V</sub>).  Typical Value = 0.05.
	 */
	public PU kv;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD1</sub> (S<sub>E</sub>[E<sub>FD1</sub>]).  Typical Value = 0.267.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage,
	 * E<sub>FD2</sub> (S<sub>E</sub>[E<sub>FD2</sub>]).  Typical Value = 0.068.
	 */
	public Float seefd2;
	/**
	 * Exciter time constant, integration rate associated with exciter control
	 * (T<sub>E</sub>).  Typical Value = 0.5.
	 */
	public Seconds te;
	/**
	 * Rheostat travel time (T<sub>RH</sub>).  Typical Value = 20.
	 */
	public Seconds trh;
	/**
	 * Maximum voltage regulator output (V<sub>RMAX</sub>).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (V<sub>RMIN</sub>).  Typical Value = 0.
	 */
	public PU vrmin;

	public ExcIEEEDC3A(){

	}
}//end ExcIEEEDC3A