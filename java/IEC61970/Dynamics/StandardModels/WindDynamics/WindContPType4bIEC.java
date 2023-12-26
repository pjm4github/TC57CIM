package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * P control model Type 4B.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.6.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContPType4bIEC extends IdentifiedObject {

	/**
	 * Maximum wind turbine power ramp rate (<i>dp</i><sub>maxp4B</sub>). It is
	 * project dependent parameter.
	 */
	public PU dpmaxp4b;
	/**
	 * Time constant in aerodynamic power response (<i>T</i><sub>paero</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds tpaero;
	/**
	 * Time constant in power order lag (<i>T</i><sub>pordp4B</sub>). It is type
	 * dependent parameter.
	 */
	public Seconds tpordp4b;
	/**
	 * Voltage measurement filter time constant (<i>T</i><sub>ufiltp4B</sub>). It is
	 * type dependent parameter.
	 */
	public Seconds tufiltp4b;
	/**
	 * Wind turbine type 4B model with which this wind control P type 4B model is
	 * associated.
	 */
	public WindTurbineType4bIEC WindTurbineType4bIEC;

	public WindContPType4bIEC(){

	}
}//end WindContPType4bIEC