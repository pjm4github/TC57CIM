package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.ActivePowerChangeRate;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ActivePower;

/**
 * Offer to supply energy/ancillary services from a load resource (participating
 * load reduces consumption).
 * @created 28-Dec-2023 5:21:50 PM
 */
public class LoadBid extends ResourceBid {

	/**
	 * Maximum rate that load can be reduced (MW/minute)
	 */
	public ActivePowerChangeRate dropRampRate;
	/**
	 * load reduction initiation cost
	 */
	public Money loadRedInitiationCost;
	/**
	 * load reduction initiation time
	 */
	public Float loadRedInitiationTime;
	/**
	 * The date represents the NextMarketDate for which the load response bids apply
	 * to.
	 */
	public DateTime marketDate;
	/**
	 * Flag indicated that the load reduction is metered. (See above)
	 * If priceSetting and meteredValue both equal 1, then the facility is eligible to
	 * set LMP in the real time market.
	 */
	public Boolean meteredValue;
	/**
	 * Minimum MW load below which it may not be reduced.
	 */
	public ActivePower minLoad;
	/**
	 * Minimum MW for a load reduction (e.g. MW rating of a discrete pump.
	 */
	public ActivePower minLoadReduction;
	/**
	 * Cost in $ at the minimum reduced load
	 */
	public Money minLoadReductionCost;
	/**
	 * Shortest period load reduction shall be maintained before load can be restored
	 * to normal levels.
	 */
	public Float minLoadReductionInterval;
	/**
	 * Shortest time that load shall be left at normal levels before a new load
	 * reduction.
	 */
	public Float minTimeBetLoadRed;
	/**
	 * Maximum rate load may be restored (MW/minute)
	 */
	public ActivePowerChangeRate pickUpRampRate;
	/**
	 * Flag to indicate that the facility can set LMP Works in tandem with Metered
	 * Value.  Greater chance of this being dynamic than the Metered Value, however,
	 * it is requested that Price Setting and Metered Value stay at the same source.
	 * Currently no customers have implemented the metering capability, but if this
	 * option is implemented, then Price Setting could become dynamic.  However,
	 * Metered Value will remain static. 
	 */
	public Boolean priceSetting;
	/**
	 * Time period that is required from an order to reduce a load to the time that it
	 * takes to get to the minimum load reduction.
	 */
	public Float reqNoticeTime;
	/**
	 * The fixed cost associated with committing a load reduction.
	 */
	public Money shutdownCost;
	public LoadReductionPriceCurve LoadReductionPriceCurve;
	public RampRateCurve RampRateCurve;

	public LoadBid(){

	}
}//end LoadBid