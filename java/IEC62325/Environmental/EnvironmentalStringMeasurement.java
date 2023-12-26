package IEC62325.Environmental;

import IEC61970.Base.Meas.StringMeasurement;

/**
 * String measurement of relevance in the environmental domain.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class EnvironmentalStringMeasurement extends StringMeasurement {

	/**
	 * Classification condition which this string measurement helps define.
	 */
	public ClassificationCondition ClassificationCondition;
	/**
	 * Observation or forecast with which this environmental string is associated.
	 */
	public EnvironmentalInformation EnvironmentalInformation;

	public EnvironmentalStringMeasurement(){

	}
}//end EnvironmentalStringMeasurement