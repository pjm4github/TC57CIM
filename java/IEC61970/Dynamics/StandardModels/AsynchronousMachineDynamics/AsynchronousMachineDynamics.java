package IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics;

import IEC61970.Base.Wires.AsynchronousMachine;
import IEC61970.Dynamics.StandardModels.RotatingMachineDynamics;

/**
 * Asynchronous machine whose behaviour is described by reference to a standard
 * model expressed in either time constant reactance form or equivalent circuit
 * form <font color="#0f0f0f">or by definition of a user-defined model.</font>
 * 
 * <b>Parameter Notes:</b>
 * <ol>
 * 	<li>Asynchronous machine parameters such as <b>Xl, Xs</b> etc. are actually
 * used as inductances (L) in the model, but are commonly referred to as
 * reactances since, at nominal frequency, the per unit values are the same.
 * However, some references use the symbol L instead of X. </li>
 * </ol>
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AsynchronousMachineDynamics extends RotatingMachineDynamics {

	/**
	 * Asynchronous machine to which this asynchronous machine dynamics model applies.
	 */
	public AsynchronousMachine AsynchronousMachine;

	public AsynchronousMachineDynamics(){

	}
}//end AsynchronousMachineDynamics