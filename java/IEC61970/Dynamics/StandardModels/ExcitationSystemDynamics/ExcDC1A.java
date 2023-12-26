package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE DC1A direct current commutator exciter with speed input and
 * without underexcitation limiters (UEL) inputs.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcDC1A extends ExcitationSystemDynamics {

	/**
	 * Maximum voltage exciter output limiter (Efdmax).  Typical Value = 99.
	 */
	public PU edfmax;
	/**
	 * Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
	 * 3.1.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
	 * 2.3.
	 */
	public PU efd2;
	/**
	 * Minimum voltage exciter output limiter (Efdmin).  Typical Value = -99.
	 */
	public PU efdmin;
	/**
	 * (exclim).
	 * IEEE standard is ambiguous about lower limit on exciter output.
	 * true = a lower limit of zero is applied to integrator output
	 * false = a lower limit of zero is not applied to integrator output.
	 * Typical Value = true.
	 */
	public Boolean exclim;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 46.
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 0.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gain (Kf).  Typical Value = 0.1.
	 */
	public PU kf;
	/**
	 * Coefficient to allow different usage of the model-speed coefficient (Ks).
	 * Typical Value = 0.
	 */
	public PU ks;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Efd1
	 * (Se[Eefd1]).  Typical Value = 0.33.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Efd1
	 * (Se[Eefd1]).  Typical Value = 0.33.
	 */
	public Float seefd2;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.06.
	 */
	public Seconds ta;
	/**
	 * Voltage regulator time constant (Tb).  Typical Value = 0.
	 */
	public Seconds tb;
	/**
	 * Voltage regulator time constant (Tc).  Typical Value = 0.
	 */
	public Seconds tc;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 * Typical Value = 0.46.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 1.
	 */
	public Seconds tf;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = -0.9.
	 */
	public PU vrmin;

	public ExcDC1A(){

	}
}//end ExcDC1A