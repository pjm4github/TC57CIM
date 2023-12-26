package IEC61970.Dynamics.StandardModels.SynchronousMachineDynamics;

import IEC61970.Base.Wires.SynchronousMachine;
import IEC61970.Dynamics.StandardModels.TurbineGovernorDynamics.TurbineGovernorDynamics;
import IEC61970.Dynamics.StandardModels.RotatingMachineDynamics;

/**
 * Synchronous machine whose behaviour is described by reference to a standard
 * model expressed in one of the following forms:
 * <ul>
 * 	<li>simplified (or classical), where a group of generators or motors is not
 * modelled in detail</li>
 * </ul>
 * <ul>
 * 	<li>detailed, in equivalent circuit form</li>
 * 	<li>detailed, in time constant reactance form</li>
 * </ul>
 * <font color="#0f0f0f">or by definition of a user-defined model.</font>
 * <font color="#0f0f0f">
 * </font><font color="#0f0f0f"><b>Note:</b>  It is a common practice to represent
 * small generators by a negative load rather than by a dynamic generator model
 * when performing dynamics simulations. In this case a SynchronousMachine in the
 * static model is not represented by anything in the dynamics model, instead it
 * is treated as ordinary load.</font>
 * <font color="#0f0f0f">
 * </font><font color="#0f0f0f"><b>Parameter Notes:</b></font>
 * <ol>
 * 	<li><font color="#0f0f0f">Synchronous machine parameters such as <b>Xl, Xd</b>,
 * <b> Xp</b> etc. are actually used as inductances (L) in the models,</font> but
 * are commonly referred to as reactances since, at nominal frequency, the per
 * unit values are the same. However, some references use the symbol L instead of
 * X. </li>
 * </ol>
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class SynchronousMachineDynamics extends RotatingMachineDynamics {

	/**
	 * Synchronous machine to which synchronous machine dynamics model applies.
	 */
	public SynchronousMachine SynchronousMachine;
	/**
	 * Turbine-governor model associated with this synchronous machine model.
	 */
	public TurbineGovernorDynamics TurbineGovernorDynamics;

	public SynchronousMachineDynamics(){

	}
}//end SynchronousMachineDynamics