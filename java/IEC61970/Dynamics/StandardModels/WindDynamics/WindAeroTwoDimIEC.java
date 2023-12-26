package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.AngleDegrees;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Two-dimensional aerodynamic model.
 * 
 * Reference: IEC Standard 614000-27-1 Section 5.6.1.3.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindAeroTwoDimIEC extends IdentifiedObject {

	/**
	 * Partial derivative of aerodynamic power with respect to changes in WTR speed
	 * (<i>dp</i><i><sub>omega</sub></i>). It is type dependent parameter.
	 */
	public PU dpomega;
	/**
	 * Partial derivative of aerodynamic power with respect to changes in pitch angle
	 * (<i>dp</i><i><sub>theta</sub></i>). It is type dependent parameter.
	 */
	public PU dptheta;
	/**
	 * Partial derivative (<i>dp</i><sub>v1</sub>). It is type dependent parameter.
	 */
	public PU dpv1;
	/**
	 * Rotor speed if the wind turbine is not derated
	 * (<i>omega</i><i><sub>0</sub></i>). It is type dependent parameter.
	 */
	public PU omegazero;
	/**
	 * Available aerodynamic power (<i>p</i><sub>avail</sub>). It is case dependent
	 * parameter.
	 */
	public PU pavail;
	/**
	 * Blade angle at twice rated wind speed (<i>theta</i><i><sub>v2</sub></i>). It is
	 * type dependent parameter.
	 */
	public AngleDegrees thetav2;
	/**
	 * Pitch angle if the wind turbine is not derated
	 * (<i>theta</i><i><sub>0</sub></i>). It is case dependent parameter.
	 */
	public AngleDegrees thetazero;
	/**
	 * Wind turbine type 3 model with which this wind aerodynamic model is associated.
	 */
	public WindTurbineType3IEC WindTurbineType3IEC;

	public WindAeroTwoDimIEC(){

	}
}//end WindAeroTwoDimIEC