package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.PerCent;

/**
 * To model the startup costs of a generation resource.
 * @author USRAKHA
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourceStartupCost {

	/**
	 * Verifiable Cold Start Up Fuel (MMBtu per start)
	 */
	public Float fuelColdStartup;
	/**
	 * Verifiable Hot Start Up Fuel (MMBtu per start)
	 */
	public Float fuelHotStartup;
	/**
	 * Verifiable Intermediate Start Up Fuel (MMBtu per start)
	 */
	public Float fuelIntermediateStartup;
	/**
	 * Minimum-Energy fuel, MMBtu/MWh
	 */
	public Float fuelLowSustainedLimit;
	/**
	 * Percentage of Fuel Index Price (gas) for cold startup
	 */
	public PerCent gasPercentColdStartup;
	/**
	 * Percentage of Fuel Index Price (gas) for hot startup
	 */
	public PerCent gasPercentHotStartup;
	/**
	 * Percentage of Fuel Index Price (gas) for intermediate startup
	 */
	public PerCent gasPercentIntermediateStartup;
	/**
	 * Percentage of FIP (gas) for operating at LSL
	 */
	public PerCent gasPercentLowSustainedLimit;
	/**
	 * Percentage of Fuel Oil Price (FOP) for cold startup
	 */
	public PerCent oilPercentColdStartup;
	/**
	 * Percentage of Fuel Oil Price (FOP) for hot startup
	 */
	public PerCent oilPercentHotStartup;
	/**
	 * Percentage of Fuel Oil Price (FOP) for intermediate startup
	 */
	public PerCent oilPercentIntermediateStartup;
	/**
	 * Percentage of FOP (oil) for operating at LSL
	 */
	public PerCent oilPercentLowSustainedLimit;
	/**
	 * Percentage of Solid Fuel for cold startup
	 */
	public PerCent solidfuelPercentColdStartup;
	/**
	 * Percentage of Solid Fuel for hot startup
	 */
	public PerCent solidfuelPercentHotStartup;
	/**
	 * Percentage of Solid Fuel for intermedite startup
	 */
	public PerCent solidfuelPercentIntermediateStartup;
	/**
	 * Percentage of Solid Fuel for operating at LSL
	 */
	public PerCent solidfuelPercentLowSustainedLimit;

	public ResourceStartupCost(){

	}
}//end ResourceStartupCost