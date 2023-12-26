package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Czech Proportion/Integral Exciter.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcCZ extends ExcitationSystemDynamics {

	/**
	 * Exciter output maximum limit (Efdmax).
	 */
	public PU efdmax;
	/**
	 * Exciter output minimum limit (Efdmin). 
	 */
	public PU efdmin;
	/**
	 * Regulator gain (Ka).
	 */
	public PU ka;
	/**
	 * Exciter constant related to self-excited field (Ke).
	 */
	public PU ke;
	/**
	 * Regulator proportional gain (Kp).
	 */
	public PU kp;
	/**
	 * Regulator time constant (Ta).
	 */
	public Seconds ta;
	/**
	 * Regulator integral time constant (Tc). 
	 */
	public Seconds tc;
	/**
	 * Exciter time constant, integration rate associated with exciter control (Te).
	 */
	public Seconds te;
	/**
	 * Voltage regulator maximum limit (Vrmax). 
	 */
	public PU vrmax;
	/**
	 * Voltage regulator minimum limit (Vrmin). 
	 */
	public PU vrmin;

	public ExcCZ(){

	}
}//end ExcCZ