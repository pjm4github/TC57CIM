package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Seconds;

/**
 * IEC Type 3A generator set model.
 * 
 * Reference: IEC Standard 61400-27-1 Section 5.6.3.2.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindGenType3aIEC extends WindGenType3IEC {

	/**
	 * Current PI controller proportional gain (K<sub>Pc</sub>). It is type dependent
	 * parameter.
	 */
	public Float kpc;
	/**
	 * Current PI controller integration time constant (T<sub>Ic</sub>). It is type
	 * dependent parameter.
	 */
	public Seconds tic;
	/**
	 * Wind turbine type 4 model with which this wind generator type 3A model is
	 * associated.
	 */
	public WindTurbineType4IEC WindTurbineType4IEC;

	public WindGenType3aIEC(){

	}
}//end WindGenType3aIEC