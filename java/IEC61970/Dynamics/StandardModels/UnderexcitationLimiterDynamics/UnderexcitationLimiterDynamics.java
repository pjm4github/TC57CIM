package IEC61970.Dynamics.StandardModels.UnderexcitationLimiterDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics;
import IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal;

/**
 * Underexcitation limiter function block whose behaviour is described by
 * reference to a standard model <font color="#0f0f0f">or by definition of a user-
 * defined model.</font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class UnderexcitationLimiterDynamics extends DynamicsFunctionBlock {

	/**
	 * Excitation system model with which this underexcitation limiter model is
	 * associated.
	 */
	public ExcitationSystemDynamics ExcitationSystemDynamics;
	/**
	 * Remote input signal used by this underexcitation limiter model.
	 */
	public RemoteInputSignal RemoteInputSignal;

	public UnderexcitationLimiterDynamics(){

	}
}//end UnderexcitationLimiterDynamics