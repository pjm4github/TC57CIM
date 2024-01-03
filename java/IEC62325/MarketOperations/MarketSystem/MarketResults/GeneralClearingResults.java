package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Float;

/**
 * Provides the adjusted load forecast value on a load forecast zone basis.
 * @created 28-Dec-2023 8:21:31 PM
 */
public class GeneralClearingResults {

	/**
	 * Load Prediction/Forecast (MW), by Time Period (5', 10', 15')
	 */
	public ActivePower loadForecast;
	/**
	 * Amount of load in the control zone
	 * Attribute Usage: hourly load value for the specific area
	 */
	public Float totalLoad;
	/**
	 * Amount of interchange for the control zone
	 * Attribute Usage: hourly interchange value for the specific area
	 */
	public Float totalNetInterchange;

	public GeneralClearingResults(){

	}
}//end GeneralClearingResults