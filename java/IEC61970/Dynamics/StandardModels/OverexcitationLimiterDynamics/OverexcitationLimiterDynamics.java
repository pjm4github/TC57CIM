package IEC61970.Dynamics.StandardModels.OverexcitationLimiterDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics;

/**
 * <font color="#0f0f0f">O</font>Overexcitation limiter function block whose
 * behaviour is described by reference to a standard model <font
 * color="#0f0f0f">or by definition of a user-defined model.</font>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class OverexcitationLimiterDynamics extends DynamicsFunctionBlock {

	/**
	 * Excitation system model with which this overexcitation limiter model is
	 * associated.
	 */
	public ExcitationSystemDynamics ExcitationSystemDynamics;

	public OverexcitationLimiterDynamics(){

	}
}//end OverexcitationLimiterDynamics