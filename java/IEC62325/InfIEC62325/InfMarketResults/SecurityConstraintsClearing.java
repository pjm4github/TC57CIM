package IEC62325.InfIEC62325.InfMarketResults;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Money;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Binding security constrained clearing results posted for a given settlement
 * period.
 * @created 03-Jan-2024 1:54:12 PM
 */
public class SecurityConstraintsClearing extends MarketFactors {

	/**
	 * Optimal MW flow
	 */
	public ActivePower mwFlow;
	/**
	 * Binding MW limit.
	 */
	public ActivePower mwLimit;
	/**
	 * Security constraint shadow price.
	 */
	public Money shadowPrice;

	public SecurityConstraintsClearing(){

	}
}//end SecurityConstraintsClearing