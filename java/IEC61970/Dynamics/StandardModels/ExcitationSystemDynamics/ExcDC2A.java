package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * Modified IEEE DC2A direct current commutator exciters with speed input, one
 * more leg block in feedback loop and without underexcitation limiters (UEL)
 * inputs.  DC type 2 excitation system model with added speed multiplier, added
 * lead-lag, and voltage-dependent limits.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcDC2A extends ExcitationSystemDynamics {

	/**
	 * Exciter voltage at which exciter saturation is defined (Efd1).  Typical Value =
	 * 3.05.
	 */
	public PU efd1;
	/**
	 * Exciter voltage at which exciter saturation is defined (Efd2).  Typical Value =
	 * 2.29.
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
	 * Voltage regulator gain (Ka).  Typical Value = 300.
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (Ke).  If Ke is entered as zero,
	 * the model calculates an effective value of Ke such that the initial condition
	 * value of Vr is zero. The zero value of Ke is not changed.  If Ke is entered as
	 * non-zero, its value is used directly, without change.  Typical Value = 1.
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
	 * (Se[Eefd1]).  Typical Value = 0.279.
	 */
	public Float seefd1;
	/**
	 * Exciter saturation function value at the corresponding exciter voltage, Efd2
	 * (Se[Efd2]).  Typical Value = 0.117.
	 */
	public Float seefd2;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.01.
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
	 * Typical Value = 1.33.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675.
	 */
	public Seconds tf;
	/**
	 * Excitation control system stabilizer time constant (Tf1).  Typical Value = 0.
	 */
	public Seconds tf1;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 4.95.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = -4.9.
	 */
	public PU vrmin;
	/**
	 * (Vtlim).
	 * true = limiter at the block [Ka/(1+sTa)] is dependent on Vt
	 * false = limiter at the block is not dependent on Vt.
	 * Typical Value = true.
	 */
	public Boolean vtlim;

	public ExcDC2A(){

	}
}//end ExcDC2A