package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;

/**
 * IEC Type 3B generator set model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.3.3.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindGenType3bIEC extends WindGenType3IEC {

	/**
	 * Crowbar control mode (<i>M</i><sub>WTcwp</sub>).
	 * <ul>
	 * 	<li>true = 1 in the model</li>
	 * 	<li>false = 0 in the model.</li>
	 * </ul>
	 * The parameter is case dependent parameter.
	 */
	public Boolean mwtcwp;
	/**
	 * Current generation Time constant (<i>T</i><sub>g</sub>). It is type dependent
	 * parameter.
	 */
	public Seconds tg;
	/**
	 * Time constant for crowbar washout filter (<i>T</i><sub>wo</sub>). It is case
	 * dependent parameter.
	 */
	public Seconds two;

	public WindGenType3bIEC(){

	}
}//end WindGenType3bIEC