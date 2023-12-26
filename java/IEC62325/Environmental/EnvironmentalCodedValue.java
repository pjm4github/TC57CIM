package IEC62325.Environmental;

import IEC62325.Environmental.EnvDomain.CoverageCodeKind;
import IEC62325.Environmental.EnvDomain.IntensityCodeKind;
import IEC61970.Base.Domain.PerCent;
import IEC62325.Environmental.EnvDomain.WeatherCodeKind;
import IEC61970.Base.Meas.StringMeasurementValue;

/**
 * An environmental value described using a coded value. A triplicate of
 * enumerated values representing intensity, coverage, type of weather is used.
 * These may be concatenated into the string value.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class EnvironmentalCodedValue extends StringMeasurementValue {

	/**
	 * Code representing the coverage of the weather condition.
	 */
	public CoverageCodeKind coverageKind;
	/**
	 * Code representing the intensity of the weather condition.
	 */
	public IntensityCodeKind intensityKind;
	/**
	 * Probability of weather condition occurring during the time interval expressed
	 * as a percentage. Applicable only when weather condition is related to a
	 * forecast (not an observation).
	 */
	public PerCent probabilityPercent;
	/**
	 * Code representing the type of weather condition.
	 */
	public WeatherCodeKind weatherKind;

	public EnvironmentalCodedValue(){

	}
}//end EnvironmentalCodedValue