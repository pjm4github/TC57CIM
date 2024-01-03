package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This class represents planned events. Used to model the various planned events
 * in a market (closing time, clearing time, etc.)
 * @created 28-Dec-2023 8:12:55 PM
 */
public class PlannedMarketEvent extends IdentifiedObject {

	/**
	 * Planned event type.
	 */
	public String eventType;
	/**
	 * This is relative time so that this attribute can be used by more than one
	 * planned market. For example the bid submission is 10am everyday.
	 */
	public Integer plannedTime;

	public PlannedMarketEvent(){

	}
}//end PlannedMarketEvent