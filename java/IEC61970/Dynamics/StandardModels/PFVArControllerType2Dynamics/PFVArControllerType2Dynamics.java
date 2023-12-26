package IEC61970.Dynamics.StandardModels.PFVArControllerType2Dynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics;

/**
 * Power Factor or VAr controller Type II function block whose behaviour is
 * described by reference to a standard model <font color="#0f0f0f">or by
 * definition of a user-defined model.</font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PFVArControllerType2Dynamics extends DynamicsFunctionBlock {

	/**
	 * Excitation system model with which this Power Factor or VAr controller Type II
	 * is associated.
	 */
	public ExcitationSystemDynamics ExcitationSystemDynamics;

	public PFVArControllerType2Dynamics(){

	}
}//end PFVArControllerType2Dynamics