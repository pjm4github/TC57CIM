package IEC61970.Dynamics.StandardModels.WindDynamics;


/**
 * Simplified IEC type plant level model.
 * 
 * Reference: IEC 61400-27-1, Annex D.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindPlantIEC extends WindPlantDynamics {

	/**
	 * Wind plant model with which this wind reactive control is associated.
	 */
	public WindPlantReactiveControlIEC WindPlantReactiveControlIEC;

	public WindPlantIEC(){

	}
}//end WindPlantIEC