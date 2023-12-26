package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;

/**
 * Manual excitation control with field circuit resistance. This model can be used
 * as a very simple representation of manual voltage control.
 * @author pcha006
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class ExcAVR5 extends ExcitationSystemDynamics {

	/**
	 * Gain (Ka).
	 */
	public PU ka;
	/**
	 * Effective Output Resistance (Rex). Rex represents the effective output
	 * resistance seen by the excitation system.
	 */
	public PU rex;
	/**
	 * Time constant (Ta).
	 */
	public Seconds ta;

	public ExcAVR5(){

	}
}//end ExcAVR5