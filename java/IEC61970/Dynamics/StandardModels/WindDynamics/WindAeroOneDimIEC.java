package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.AngleDegrees;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * One-dimensional aerodynamic model.
 * 
 * Reference: IEC Standard 614000-27-1 Section 5.6.1.2.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindAeroOneDimIEC extends IdentifiedObject {

	/**
	 * Aerodynamic gain (<i>k</i><i><sub>a</sub></i>). It is type dependent parameter.
	 */
	public Float ka;
	/**
	 * Initial pitch angle (<i>theta</i><i><sub>omega0</sub></i>). It is case
	 * dependent parameter.
	 */
	public AngleDegrees thetaomega;
	/**
	 * Wind turbine type 3 model with which this wind aerodynamic model is associated.
	 */
	public WindTurbineType3IEC WindTurbineType3IEC;

	public WindAeroOneDimIEC(){

	}
}//end WindAeroOneDimIEC