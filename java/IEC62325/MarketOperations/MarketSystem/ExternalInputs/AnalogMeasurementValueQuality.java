package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Meas.MeasurementValueQuality;

/**
 * Measurement quality flags for Analog Values.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class AnalogMeasurementValueQuality extends MeasurementValueQuality {

	/**
	 * The quality code for the given Analog Value.
	 */
	public String scadaQualityCode;

	public AnalogMeasurementValueQuality(){

	}
}//end AnalogMeasurementValueQuality