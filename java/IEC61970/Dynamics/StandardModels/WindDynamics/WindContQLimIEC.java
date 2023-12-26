package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Constant Q limitation model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.5.9.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindContQLimIEC extends IdentifiedObject {

	/**
	 * Maximum reactive power (<i>q</i><sub>max</sub>). It is type dependent parameter.
	 */
	public PU qmax;
	/**
	 * Minimum reactive power (<i>q</i><sub>min</sub>). It is type dependent parameter.
	 */
	public PU qmin;
	/**
	 * Wind generator type 3 or 4 model with which this constant Q limitation model is
	 * associated.
	 */
	public WindTurbineType3or4IEC WindTurbineType3or4IEC;

	public WindContQLimIEC(){

	}
}//end WindContQLimIEC