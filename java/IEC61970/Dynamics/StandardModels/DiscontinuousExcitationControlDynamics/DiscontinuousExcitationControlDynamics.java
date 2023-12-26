package IEC61970.Dynamics.StandardModels.DiscontinuousExcitationControlDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics;
import IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal;

/**
 * Discontinuous excitation control function block whose behaviour is described by
 * reference to a standard model <font color="#0f0f0f">or by definition of a user-
 * defined model</font>.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class DiscontinuousExcitationControlDynamics extends DynamicsFunctionBlock {

	/**
	 * Excitation system model with which this discontinuous excitation control model
	 * is associated.
	 */
	public ExcitationSystemDynamics ExcitationSystemDynamics;
	/**
	 * Remote input signal used by this discontinuous excitation control system model.
	 */
	public RemoteInputSignal RemoteInputSignal;

	public DiscontinuousExcitationControlDynamics(){

	}
}//end DiscontinuousExcitationControlDynamics