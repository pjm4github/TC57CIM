package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.RegularIntervalSchedule;

/**
 * Represents the performance of a resource as time series data for a specified
 * time period, time interval, and evaluation criteria.
 * @author mwald
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourcePerformanceTimeSeriesFactor extends RegularIntervalSchedule {

	/**
	 * Type of the time series data, e.g. baseline data, meter read data, computed
	 * performance data.
	 */
	public String timeSeriesDataType;
	/**
	 * Optional description of the time series data, e.g. baseline data, meter read
	 * data, computed performance data.
	 */
	public String timeSeriesDescription;
	/**
	 * Description for the value1 contained within the TimeSeriesFactor.
	 */
	public String value1Description;
	/**
	 * Description for the value2 contained within the TimeSeriesFactor.
	 */
	public String value2Description;

	public ResourcePerformanceTimeSeriesFactor(){

	}
}//end ResourcePerformanceTimeSeriesFactor