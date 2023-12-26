package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Reference frame rotation model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.3.5.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindRefFrameRotIEC extends IdentifiedObject {

	/**
	 * Time constant for PLL first order filter model (T<sub>PLL</sub>). It is type
	 * dependent parameter.
	 */
	public Seconds tpll;
	/**
	 * Voltage below which the angle of the voltage is filtered and possibly also
	 * frozen (u<sub>PLL1</sub>). It is type dependent parameter.
	 */
	public PU upll1;
	/**
	 * Voltage (u<sub>PLL2</sub>) below which the angle of the voltage is frozen if
	 * u<sub>PLL2 </sub>is smaller or equal to u<sub>PLL1</sub> . It is type dependent
	 * parameter.
	 */
	public PU upll2;
	/**
	 * Wind turbine type 3 or 4 model with which this reference frame rotation model
	 * is associated.
	 */
	public WindTurbineType3or4IEC WindTurbineType3or4IEC;

	public WindRefFrameRotIEC(){

	}
}//end WindRefFrameRotIEC