package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Two mass model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.2.1.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindMechIEC extends IdentifiedObject {

	/**
	 * Drive train damping (<i>c</i><i><sub>drt</sub></i><i>)</i>. It is type
	 * dependent parameter.
	 */
	public PU cdrt;
	/**
	 * Inertia constant of generator (<i>H</i><sub>gen</sub>). It is type dependent
	 * parameter.
	 */
	public Seconds hgen;
	/**
	 * Inertia constant of wind turbine rotor (<i>H</i><sub>WTR</sub>). It is type
	 * dependent parameter.
	 */
	public Seconds hwtr;
	/**
	 * Drive train stiffness (<i>k</i><i><sub>drt</sub></i>). It is type dependent
	 * parameter.
	 */
	public PU kdrt;
	/**
	 * Wind turbine type 4B model with which this wind mechanical model is associated.
	 */
	public WindTurbineType4bIEC WindTurbineType4bIEC;
	/**
	 * Wind turbine Type 3 model with which this wind mechanical model is associated.
	 */
	public WindTurbineType3IEC WindTurbineType3IEC;
	/**
	 * Wind generator type 1 or 2 model with which this wind mechanical model is
	 * associated.
	 */
	public WindTurbineType1or2IEC WindTurbineType1or2IEC;

	public WindMechIEC(){

	}
}//end WindMechIEC