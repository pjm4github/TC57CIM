package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.MktDomain.ResourceLimitIndicator;
import IEC62325.MarketOperations.MktDomain.YesNo;

/**
 * Provides all Region Ancillary Service results for the DA and RT markets. The
 * specific data is commodity type (Regulation Up, Regulation Down, Spinning
 * Reserve, Non-spinning Reserve, or Total Up reserves) based for the cleared MW,
 * cleared price, and total capacity required for the region.
 * @created 28-Dec-2023 8:23:02 PM
 */
public class MarketRegionResults {

	/**
	 * Cleared generation Value in MW.  For AS, this value is clearedMW = AS Total.
	 * For AS, clearedMW - selfScheduleMW = AS Procured
	 */
	public Float clearedMW;
	/**
	 * Marginal Price ($/MW) for the commodity (Energy, Regulation Up, Regulation Down,
	 * Spinning Reserve, or Non-spinning reserve) based on the pricing run.
	 */
	public Float clearedPrice;
	/**
	 * Dispatchable MW for Combustion units.
	 */
	public Float dispatchCtMW;
	/**
	 * Dispatchable MW for Hydro units.
	 */
	public Float dispatchHydroMW;
	/**
	 * Dispatch rate in MW/minutes.
	 */
	public Float dispatchRate;
	/**
	 * Dispatchable MW for Steam units.
	 */
	public Float dispatchSteamMW;
	/**
	 * Imbalance Energy Bias (MW) by Time Period (5' only)
	 */
	public Float imbalanceEnergyBias;
	/**
	 * Locational AS Flags indicating whether the Upper or Lower Bound limit of the AS
	 * regional procurment is binding
	 */
	public ResourceLimitIndicator limitFlag;
	/**
	 * The "Lumpy Flag"(Y/N)  indicates whether the resource that sets the price is a
	 * lumpy generator by hour over the time horizon.
	 * 
	 * Only applicable for the Day Ahead Market
	 */
	public YesNo lumpyIndicator;
	/**
	 * Region requirement maximum limit
	 */
	public Float maxSufficiencyIndex;
	/**
	 * Region requirement minimum limit
	 */
	public Float minSufficiencyIndex;
	/**
	 * Region requirement maximum limit
	 */
	public Float reqMaxMW;
	/**
	 * Region requirement minimum limit
	 */
	public Float reqMinMW;
	/**
	 * Aof AS, selfScheduleMW = AS Self-Provided
	 */
	public Float selfScheduleMW;

	public MarketRegionResults(){

	}
}//end MarketRegionResults