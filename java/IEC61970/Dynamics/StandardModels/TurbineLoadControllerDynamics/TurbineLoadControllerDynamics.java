package IEC61970.Dynamics.StandardModels.TurbineLoadControllerDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics;

/**
 * Turbine load controller function block whose behavior is described by reference
 * to a standard model <font color="#0f0f0f">or by definition of a user-defined
 * model.</font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TurbineLoadControllerDynamics extends DynamicsFunctionBlock {

	/**
	 * Turbine-governor controlled by this turbine load controller.
	 */
	public TurbineGovernorDynamics TurbineGovernorDynamics;

	public TurbineLoadControllerDynamics(){

	}
}//end TurbineLoadControllerDynamics