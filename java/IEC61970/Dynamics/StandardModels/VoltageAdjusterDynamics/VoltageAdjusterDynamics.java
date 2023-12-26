package IEC61970.Dynamics.StandardModels.VoltageAdjusterDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.PFVArControllerType1Dynamics.PFVArControllerType1Dynamics;

/**
 * Voltage adjuster function block whose behaviour is described by reference to a
 * standard model <font color="#0f0f0f">or by definition of a user-defined model.
 * </font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class VoltageAdjusterDynamics extends DynamicsFunctionBlock {

	/**
	 * Power Factor or VAr controller Type I model with which this voltage adjuster is
	 * associated.
	 */
	public PFVArControllerType1Dynamics PFVArControllerType1Dynamics;

	public VoltageAdjusterDynamics(){

	}
}//end VoltageAdjusterDynamics