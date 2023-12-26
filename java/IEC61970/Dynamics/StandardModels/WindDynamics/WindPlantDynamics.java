package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Dynamics.StandardModels.DynamicsFunctionBlock;
import IEC61970.Dynamics.StandardInterconnections.RemoteInputSignal;

/**
 * Parent class supporting relationships to wind turbines Type 3 and 4 and wind
 * plant IEC and user defined wind plants including their control models.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindPlantDynamics extends DynamicsFunctionBlock {

	/**
	 * The wind turbine type 3 or 4 associated with this wind plant.
	 */
	public WindTurbineType3or4Dynamics WindTurbineType3or4Dynamics;
	/**
	 * The remote signal with which this power plant is associated.
	 */
	public RemoteInputSignal RemoteInputSignal;

	public WindPlantDynamics(){

	}
}//end WindPlantDynamics