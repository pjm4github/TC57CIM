package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Parent class supporting relationships to IEC wind turbines Type 3 generator
 * models of IEC type 3A and 3B.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindGenType3IEC extends IdentifiedObject {

	/**
	 * Maximum active current ramp rate (di<sub>pmax</sub>). It is project dependent
	 * parameter.
	 */
	public PU dipmax;
	/**
	 * Maximum reactive current ramp rate (di<sub>qmax</sub>). It is project dependent
	 * parameter.
	 */
	public PU diqmax;
	/**
	 * Electromagnetic transient reactance (x<sub>S</sub>). It is type dependent
	 * parameter.
	 */
	public PU xs;
	/**
	 * Wind turbine type 3 model with which this wind generator type 3 is associated. 
	 */
	public WindTurbineType3IEC WindTurbineType3IEC;

	public WindGenType3IEC(){

	}
}//end WindGenType3IEC