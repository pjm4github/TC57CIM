package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Boolean;

/**
 * Modified IEEE ST2A static excitation system - another lead-lag block added to
 * match  the model defined by WECC.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcST2A extends ExcitationSystemDynamics {

	/**
	 * Maximum field voltage (Efdmax).  Typical Value = 99.
	 */
	public PU efdmax;
	/**
	 * Voltage regulator gain (Ka).  Typical Value = 120.
	 */
	public PU ka;
	/**
	 * Rectifier loading factor proportional to commutating reactance (Kc).  Typical
	 * Value = 1.82.
	 */
	public PU kc;
	/**
	 * Exciter constant related to self-excited field (Ke).  Typical Value = 1.
	 */
	public PU ke;
	/**
	 * Excitation control system stabilizer gains (Kf).  Typical Value = 0.05.
	 */
	public PU kf;
	/**
	 * Potential circuit gain coefficient (Ki).  Typical Value = 8.
	 */
	public PU ki;
	/**
	 * Potential circuit gain coefficient (Kp).  Typical Value = 4.88.
	 */
	public PU kp;
	/**
	 * Voltage regulator time constant (Ta).  Typical Value = 0.15.
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
	 * Typical Value = 0.5.
	 */
	public Seconds te;
	/**
	 * Excitation control system stabilizer time constant (Tf).  Typical Value = 0.7.
	 */
	public Seconds tf;
	/**
	 * UEL input (UELin).
	 * true = HV gate
	 * false = add to error signal.
	 * Typical Value = false.
	 */
	public Boolean uelin;
	/**
	 * Maximum voltage regulator outputs (Vrmax).  Typical Value = 1.
	 */
	public PU vrmax;
	/**
	 * Minimum voltage regulator outputs (Vrmin).  Typical Value = -1.
	 */
	public PU vrmin;

	public ExcST2A(){

	}
}//end ExcST2A