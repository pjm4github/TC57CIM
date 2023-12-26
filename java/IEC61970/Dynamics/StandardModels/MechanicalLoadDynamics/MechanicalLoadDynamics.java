package IEC61970.Dynamics.StandardModels.MechanicalLoadDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics;
import IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics;

/**
 * Mechanical load function block whose behavior is described by reference to a
 * standard model <font color="#0f0f0f">or by definition of a user-defined model.
 * </font>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class MechanicalLoadDynamics extends DynamicsFunctionBlock {

	/**
	 * Asynchronous machine model with which this mechanical load model is associated.
	 */
	public AsynchronousMachineDynamics AsynchronousMachineDynamics;
	/**
	 * Synchronous machine model with which this mechanical load model is associated.
	 */
	public SynchronousMachineDynamics SynchronousMachineDynamics;

	public MechanicalLoadDynamics(){

	}
}//end MechanicalLoadDynamics