package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Meas.MeasurementValueQuality;

/**
 * Measurement quality flags for Discrete Values.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class DiscreteMeasurementValueQuality extends MeasurementValueQuality {

	/**
	 * Switch Manual Replace Indicator. Flag indicating that the switch is manual
	 * replace.
	 */
	public Boolean manualReplaceIndicator;
	/**
	 * Removed From Operation Indicator. Flag indicating that the switch is removed
	 * from operation.
	 */
	public Boolean removeFromOperationIndicator;

	public DiscreteMeasurementValueQuality(){

	}
}//end DiscreteMeasurementValueQuality