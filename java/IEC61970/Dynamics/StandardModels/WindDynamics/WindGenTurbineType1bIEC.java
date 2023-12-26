package IEC61970.Dynamics.StandardModels.WindDynamics;


/**
 * Wind turbine IEC Type 1B.
 * 
 * Reference: IEC Standard 61400-27-1, section 5.5.2.3.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindGenTurbineType1bIEC extends WindTurbineType1or2IEC {

	/**
	 * Pitch control power model associated with this wind turbine type 1B model.
	 */
	public WindPitchContPowerIEC WindPitchContPowerIEC;

	public WindGenTurbineType1bIEC(){

	}
}//end WindGenTurbineType1bIEC