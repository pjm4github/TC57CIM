package IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics.SynchronousMachineDynamics;

/**
 * Excitation system function block whose behavior is described by reference to a
 * standard model <font color="#0f0f0f">or by definition of a user-defined model.
 * </font>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:57 PM
 */
public class ExcitationSystemDynamics extends DynamicsFunctionBlock {

	/**
	 * Synchronous machine model with which this excitation system model is associated.
	 */
	public SynchronousMachineDynamics SynchronousMachineDynamics;

	public ExcitationSystemDynamics(){

	}
}//end ExcitationSystemDynamics