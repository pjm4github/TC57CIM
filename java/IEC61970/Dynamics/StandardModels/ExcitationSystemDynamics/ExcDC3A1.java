package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * This is modified old IEEE type 3 excitation system.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcDC3A1 extends ExcitationSystemDynamics {

	/**
	 * (exclim).
	 * true = lower limit of zero is applied to integrator output
	 * false = lower limit of zero not applied to integrator output.
	 * Typical Value = true.
	 */
	public Boolean exclim;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 300.
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gain (Kf).  Typical Value = 0.1.
	 */
	public PU kf;
	/**
	 * Potential circuit gain coefficient (Ki).  Typical Value = 4.83.
	 */
	public PU ki;
	/**
	 * Potential circuit gain coefficient (Kp).  Typical Value = 4.37.
	 */
	public PU kp;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.01.
	 */
	public Seconds ta;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 * Typical Value = 1.83.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 0.675.
	 */
	public Seconds tf;
	/**
	 * Available exciter voltage limiter (Vb1max).  Typical Value = 11.63.
	 */
	public PU vb1max;
	/**
	 * Vb limiter indicator.
	 * true = exciter Vbmax limiter is active
	 * false = Vb1max is active.
	 * Typical Value = true.
	 */
	public Boolean vblim;
	/**
	 * Available exciter voltage limiter (Vbmax).  Typical Value = 11.63.
	 */
	public PU vbmax;
	/**
	 * Maximum voltage regulator output (Vrmax).  Typical Value = 5.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator output (Vrmin).  Typical Value = 0.
	 */
	public PU vrmin;

	public ExcDC3A1(){

	}
}//end ExcDC3A1