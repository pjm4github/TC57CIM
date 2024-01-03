package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.YesNo;

/**
 * This class holds elements that are single values for the entire market time
 * horizon. That is, for the Day Ahead market, there is 1 value for each element,
 * not hourly based.  Is a summary of the market run.
 * @created 28-Dec-2023 8:23:09 PM
 */
public class MarketResults {

	/**
	 * Total  AS Cost (i.e., payment) ($) over the time horizon
	 */
	public Float ancillarySvcCost;
	/**
	 * Global Contingent Operating Reserve Availability Indicator (Yes/No)
	 */
	public YesNo contingentOperatingResAvail;
	/**
	 * Total Energy Cost ($) over the time horizon
	 */
	public Float energyCost;
	/**
	 * Total Minimum Load Cost ($) over the time horizon
	 */
	public Float minimumLoadCost;
	/**
	 * Total Start-up Cost ($) over the time horizon
	 */
	public Float startUpCost;
	/**
	 * Total Cost (Energy + AS) cost ($) by over the time horizon
	 */
	public Float totalCost;
	/**
	 * The total RUC capacity cost for this interval
	 */
	public Float totalRucCost;

	public MarketResults(){

	}
}//end MarketResults