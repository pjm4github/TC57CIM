package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * IEC Type 4 generator set model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.3.4.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindGenType4IEC extends IdentifiedObject {

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
	 * Minimum reactive current ramp rate (d<i>i</i><sub>qmin</sub>). It is case
	 * dependent parameter.
	 */
	public PU diqmin;
	/**
	 * Time constant (T<sub>g</sub>). It is type dependent parameter.
	 */
	public Seconds tg;
	/**
	 * Wind turbine type 4B model with which this wind generator type 4 model is
	 * associated.
	 */
	public WindTurbineType4bIEC WindTurbineType4bIEC;
	/**
	 * Wind turbine type 4A model with which this wind generator type 4 model is
	 * associated.
	 */
	public WindTurbineType4aIEC WindTurbineType4aIEC;

	public WindGenType4IEC(){

	}
}//end WindGenType4IEC