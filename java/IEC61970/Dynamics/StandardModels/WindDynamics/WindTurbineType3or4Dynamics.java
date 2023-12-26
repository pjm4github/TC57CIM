package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal;
import IEC61970.Base.Wires.PowerElectronicsConnection;

/**
 * Parent class supporting relationships to wind turbines Type 3 and 4 and wind
 * plant including their control models.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindTurbineType3or4Dynamics extends DynamicsFunctionBlock {

	/**
	 * Remote input signal used by these wind turbine Type 3 or 4 models.
	 */
	public RemoteInputSignal RemoteInputSignal;
	public PowerElectronicsConnection PowerElectronicsConnection;

	public WindTurbineType3or4Dynamics(){

	}
}//end WindTurbineType3or4Dynamics