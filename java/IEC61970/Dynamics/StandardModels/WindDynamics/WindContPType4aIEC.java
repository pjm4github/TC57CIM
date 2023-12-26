package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * P control model Type 4A.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.5.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContPType4aIEC extends IdentifiedObject {

	/**
	 * Maximum wind turbine power ramp rate (<i>dp</i><sub>maxp4A</sub>). It is
	 * project dependent parameter.
	 */
	public PU dpmaxp4a;
	/**
	 * Time constant in power order lag (<i>T</i><sub>pordp4A</sub>). It is type
	 * dependent parameter.
	 */
	public Seconds tpordp4a;
	/**
	 * Voltage measurement filter time constant (<i>T</i><sub>ufiltp4A</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds tufiltp4a;
	/**
	 * Wind turbine type 4A model with which this wind control P type 4A model is
	 * associated.
	 */
	public WindTurbineType4aIEC WindTurbineType4aIEC;

	public WindContPType4aIEC(){

	}
}//end WindContPType4aIEC