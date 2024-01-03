package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.MktDomain.LoadForecastType;
import IEC62325.MarketOperations.ReferenceData.AggregateNode;
import IEC61970.Base.Core.RegularIntervalSchedule;

/**
 * Area load curve definition.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class AreaLoadCurve extends RegularIntervalSchedule {

	/**
	 * Load forecast area type.
	 */
	public LoadForecastType forecastType;
	public AggregateNode AggregateNode;

	public AreaLoadCurve(){

	}
}//end AreaLoadCurve