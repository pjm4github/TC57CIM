package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * This is modified IEEE DC3A direct current commutator exciters with speed input,
 * and death band.  DC old type 4.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcDC3A extends ExcitationSystemDynamics {

	/**
	 * Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99.
	 */
	public PU edfmax;
	/**
	 * Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
	 * 2.6.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
	 * 3.45.
	 */
	public PU efd2;
	/**
	 * (Efdlim).
	 * true = exciter output limiter is active
	 * false = exciter output limiter not active.
	 * Typical Value = true.
	 */
	public Boolean efdlim;
	/**
	 * Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99.
	 */
	public PU efdmin;
	/**
	 * (exclim).  IEEE standard is ambiguous about lower limit on exciter output.
	 * true = a lower limit of zero is applied to integrator output
	 * false = a lower limit of zero not applied to integrator output.
	 * Typical Value = true.
	 */
	public Boolean exclim;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Death band (Kr).  If Kr is not zero, the voltage regulator input changes at a
	 * constant rate if Verr > Kr or Verr < -Kr as per the IEEE (1968) Type 4 model.
	 * If Kr is zero, the error signal drives the voltage regulator continuously as
	 * per the IEEE (1980) DC3 and IEEE (1992, 2005) DC3A models.  Typical Value = 0.
	 */
	public PU kr;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Fast raise/lower contact setting (Kv).  Typical Value = 0.05.
	 */
	public PU kv;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Efd1
	 * (Se[Eefd1]).  Typical Value = 0.1.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Efd2
	 * (Se[Efd2]).  Typical Value = 0.35.
	 */
	public Float seefd2;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 * Typical Value = 1.83.
	 */
	public Seconds te;
	/**
	 * Rheostat travel time (Trh).  Typical Value = 20.
	 */
	public Seconds trh;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 5.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = 0.
	 */
	public PU vrmin;

	public ExcDC3A(){

	}
}//end ExcDC3A