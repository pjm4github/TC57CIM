package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * QP and QU limitation model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.10.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContQPQULimIEC extends IdentifiedObject {

	/**
	 * Power measurement filter time constant for Q capacity
	 * (<i>T</i><sub>pfiltql</sub>). It is type dependent parameter.
	 */
	public Seconds tpfiltql;
	/**
	 * Voltage measurement filter time constant for Q capacity
	 * (<i>T</i><sub>ufiltql</sub>). It is type dependent parameter.
	 */
	public Seconds tufiltql;
	/**
	 * Wind generator type 3 or 4 model with which this QP and QU limitation model is
	 * associated.
	 */
	public WindTurbineType3or4IEC WindTurbineType3or4IEC;

	public WindContQPQULimIEC(){

	}
}//end WindContQPQULimIEC