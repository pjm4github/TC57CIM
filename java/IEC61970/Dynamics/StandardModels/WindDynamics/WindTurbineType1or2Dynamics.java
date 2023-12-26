package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardModels.AsynchronousMachineDynamics.AsynchronousMachineDynamics;
import IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal;

/**
 * Parent class supporting relationships to wind turbines Type 1 and 2 and their
 * control models.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindTurbineType1or2Dynamics extends DynamicsFunctionBlock {

	/**
	 * Asynchronous machine model with which this wind generator type 1 or 2 model is
	 * associated.
	 */
	public AsynchronousMachineDynamics AsynchronousMachineDynamics;
	/**
	 * Remote input signal used by this wind generator Type 1 or Type 2 model.
	 */
	public RemoteInputSignal RemoteInputSignal;

	public WindTurbineType1or2Dynamics(){

	}
}//end WindTurbineType1or2Dynamics