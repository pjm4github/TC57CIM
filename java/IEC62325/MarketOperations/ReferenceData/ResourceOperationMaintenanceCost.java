package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.Curve;

/**
 * To model the Operation and Maintenance (O and M) costs of a generation resource.
 * 
 * @author USRAKHA
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class ResourceOperationMaintenanceCost extends Curve {

	/**
	 * Percentage of Fuel Index Price (gas) for operating above Low Sustained Limit
	 * (LSL)
	 */
	public PerCent gasPercentAboveLowSustainedLimit;
	/**
	 * Percentage of Fuel Oil Price (FOP) for operating above Low Sustained Limit (LSL)
	 */
	public PerCent oilPercentAboveLowSustainedLimit;
	/**
	 * Verifiable O&M Cost ($), Cold Startup
	 */
	public Float omCostColdStartup;
	/**
	 * Verifiable O&M Cost ($), Hot Startup
	 */
	public Float omCostHotStartup;
	/**
	 * Verifiable O&M Cost ($), Intermediate Startup
	 */
	public Float omCostIntermediateStartup;
	/**
	 * Verifiable O&M Cost ($/MWh), LSL
	 */
	public Float omCostLowSustainedLimit;
	/**
	 * Percentage of Solid Fuel for operating above Low Sustained Limit (LSL)
	 */
	public PerCent solidfuelPercentAboveLowSustainedLimit;
	public ResourceVerifiableCosts ResourceVerifiableCosts;

	public ResourceOperationMaintenanceCost(){

	}
}//end ResourceOperationMaintenanceCost