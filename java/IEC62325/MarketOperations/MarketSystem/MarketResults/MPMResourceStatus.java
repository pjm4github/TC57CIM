package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.String;

/**
 * Model of results of Market Power tests, gives status of resource for the
 * associated interval.
 * @created 28-Dec-2023 8:22:45 PM
 */
public class MPMResourceStatus {

	/**
	 * Interval Test Status
	 * 
	 * 'N' - not applicable
	 */
	public String resourceStatus;

	public MPMResourceStatus(){

	}
}//end MPMResourceStatus