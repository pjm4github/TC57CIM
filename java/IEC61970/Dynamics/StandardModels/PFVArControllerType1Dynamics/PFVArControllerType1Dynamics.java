package IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics;
import IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal;

/**
 * Power Factor or VAr controller Type I function block whose behaviour is
 * described by reference to a standard model <font color="#0f0f0f">or by
 * definition of a user-defined model.</font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PFVArControllerType1Dynamics extends DynamicsFunctionBlock {

	/**
	 * Excitation system model with which this Power Factor or VAr controller Type I
	 * model is associated.
	 */
	public ExcitationSystemDynamics ExcitationSystemDynamics;
	/**
	 * Remote input signal used by this Power Factor or VAr controller Type I model.
	 */
	public RemoteInputSignal RemoteInputSignal;

	public PFVArControllerType1Dynamics(){

	}
}//end PFVArControllerType1Dynamics