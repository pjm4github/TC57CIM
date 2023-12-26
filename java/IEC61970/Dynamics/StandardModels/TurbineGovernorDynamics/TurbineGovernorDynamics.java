package IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics;

/**
 * Turbine-governor function block whose behavior is described by reference to a
 * standard model <font color="#0f0f0f">or by definition of a user-defined model.
 * </font>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TurbineGovernorDynamics extends DynamicsFunctionBlock {

	/**
	 * Asynchronous machine model with which this turbine-governor model is associated.
	 */
	public AsynchronousMachineDynamics AsynchronousMachineDynamics;

	public TurbineGovernorDynamics(){

	}
}//end TurbineGovernorDynamics