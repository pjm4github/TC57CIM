package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * The constant aerodynamic torque model assumes that the aerodynamic torque is
 * constant.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.1.1.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindAeroConstIEC extends IdentifiedObject {

	/**
	 * Wind turbine type 1A model with which this wind aerodynamic model is associated.
	 */
	public WindGenTurbineType1aIEC WindGenTurbineType1aIEC;

	public WindAeroConstIEC(){

	}
}//end WindAeroConstIEC