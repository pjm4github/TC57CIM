package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;

/**
 * Energy bid for generation, load, or virtual type for the whole of the market-
 * trading period (i.e., one day in day ahead market or one hour in the real time
 * market).
 * @created 28-Dec-2023 5:23:21 PM
 */
public class ResourceBid extends Bid {

	/**
	 * Aggregation flag
	 * 0: individual resource level
	 * 1: Aggregated node location
	 * 2: Aggregated price location)
	 */
	public Integer aggregationFlag;
	public String bidStatus;
	/**
	 * Energy product (commodity) type:
	 * 'En' - Energy
	 * 'Ru' - Regulation Up
	 * 'Rd' - Regulation Dn
	 * 'Sr' - Spinning Reserve
	 * 'Nr' - Non-Spinning Reserve
	 * 'Or' - Operating Reserve
	 */
	public String commodityType;
	/**
	 * contingent operating reserve availiability (Yes/No). Resource is availiable to
	 * participate with capacity only in contingency dispatch.
	 */
	public YesNo contingencyAvailFlag;
	/**
	 * A Yes indicates that this bid was created by the ISO.
	 */
	public YesNo createdISO;
	/**
	 * Maximum amount of energy per day which can be produced during the trading
	 * period in MWh
	 */
	public Float energyMaxDay;
	/**
	 * Minimum amount of energy per day which has to be produced during the trading
	 * period in MWh
	 */
	public Float energyMinDay;
	/**
	 * Market Separation Flag
	 * 
	 * 'Y' - Enforce market separation constraints for this bid
	 * 'N' - Don't enforce market separation constraints for this bid.
	 */
	public String marketSepFlag;
	/**
	 * minimum number of consecutive hours a resource shall be dispatched if bid is
	 * accepted  
	 */
	public Integer minDispatchTime;
	/**
	 * Resource loading curve type
	 * 1 - step-wise continuous loading
	 * 2 - piece-wise linear continuous loading
	 * 3 - block loading
	 */
	public Integer resourceLoadingType;
	/**
	 * Maximum number of shutdowns per day.
	 */
	public Integer shutDownsMaxDay;
	/**
	 * Maximum number of shutdowns per week.
	 */
	public Integer shutDownsMaxWeek;
	/**
	 * Maximum number of startups per day.
	 */
	public Integer startUpsMaxDay;
	/**
	 * Maximum number of startups per week.
	 */
	public Integer startUpsMaxWeek;
	/**
	 * True if bid is virtual.  Bid is assumed to be non-virtual if attribute is absent
	 */
	public Boolean virtual;
	public BidError BidError;

	public ResourceBid(){

	}
}//end ResourceBid