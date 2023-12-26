package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics;
import IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal;

/**
 * Power system stabilizer function block whose behaviour is described by
 * reference to a standard model <font color="#0f0f0f">or by definition of a user-
 * defined model.</font>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PowerSystemStabilizerDynamics extends DynamicsFunctionBlock {

	/**
	 * Excitation system model with which this power system stabilizer model is
	 * associated.
	 */
	public ExcitationSystemDynamics ExcitationSystemDynamics;
	/**
	 * Remote input signal used by this power system stabilizer model.
	 */
	public RemoteInputSignal RemoteInputSignal;

	public PowerSystemStabilizerDynamics(){

	}
}//end PowerSystemStabilizerDynamics