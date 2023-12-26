package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.EnvironmentalDiscreteKind;
import IEC61970.Base.Meas.Discrete;

/**
 * Discrete (integer) measurement of relevance in the environmental domain.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class EnvironmentalDiscrete extends Discrete {

	/**
	 * Kind of environmental discrete (integer).
	 */
	public EnvironmentalDiscreteKind kind;
	/**
	 * Observation or forecast with which this environmental discrete (integer) is
	 * associated.
	 */
	public EnvironmentalInformation EnvironmentalInformation;

	public EnvironmentalDiscrete(){

	}
}//end EnvironmentalDiscrete