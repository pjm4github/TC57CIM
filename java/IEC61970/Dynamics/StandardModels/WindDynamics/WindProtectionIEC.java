package IEC61970.Dynamics.StandardModels.WindDynamics;

import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The grid protection model includes protection against over and under voltage,
 * and against over and under frequency.
 * 
 * Reference: IEC Standard 614000-27-1 Section 5.6.6.
 * @author civanov
 * @version 1.0
 * @created 25-Dec-2023 8:32:05 PM
 */
public class WindProtectionIEC extends IdentifiedObject {

	/**
	 * Maximum rate of change of frequency (<i>dF</i><i><sub>max</sub></i>). It is
	 * type dependent parameter.
	 */
	public PU dfimax;
	/**
	 * Wind turbine over frequency protection activation threshold
	 * (<i>f</i><i><sub>over</sub></i>). It is project dependent parameter. 
	 */
	public PU fover;
	/**
	 * Wind turbine under frequency protection activation threshold
	 * (<i>f</i><i><sub>under</sub></i>). It is project dependent parameter.
	 */
	public PU funder;
	/**
	 * Zero crossing measurement mode (<i>Mzc</i>). True = 1 if the WT protection
	 * system uses zero crossings to detect frequency - otherwise false = 0. It is
	 * type dependent parameter.
	 */
	public Boolean mzc;
	/**
	 * Time interval of moving average window (<i>TfMA</i>). It is type dependent
	 * parameter.
	 */
	public Seconds tfma;
	/**
	 * Wind turbine over voltage protection activation threshold
	 * (<i>u</i><i><sub>over</sub></i>). It is project dependent parameter.
	 */
	public PU uover;
	/**
	 * Wind turbine under voltage protection activation threshold
	 * (<i>u</i><i><sub>under</sub></i>). It is project dependent parameter.
	 */
	public PU uunder;
	/**
	 * Wind generator type 3 or 4 model with which this wind turbine protection model
	 * is associated.
	 */
	public WindTurbineType3or4IEC WindTurbineType3or4IEC;
	/**
	 * Wind generator type 1 or 2 model with which this wind turbine protection model
	 * is associated.
	 */
	public WindTurbineType1or2IEC WindTurbineType1or2IEC;

	public WindProtectionIEC(){

	}
}//end WindProtectionIEC