package IEC62325.MarketOperations.ParticipantInterfaces;

import IEC62325.MarketOperations.MktDomain.MarketType;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Document;
import IEC62325.MarketOperations.MarketSystem.MarketResults.ChargeProfile;
import IEC62325.MarketOperations.MarketSystem.MarketResults.MitigatedBidSegment;
import IEC62325.MarketOperations.MarketPlan.EnergyMarket;
import IEC62325.MarketCommon.MarketParticipant;

/**
 * Represents both bids to purchase and offers to sell energy or ancillary
 * services in an RTO-sponsored market.
 * @created 28-Dec-2023 5:18:26 PM
 */
public class Bid extends Document {

	/**
	 * The market type, DAM or RTM.
	 */
	public MarketType marketType;
	/**
	 * Start time and date for which bid applies.
	 */
	public DateTime startTime;
	/**
	 * Stop time and date for which bid is applicable.
	 */
	public DateTime stopTime;
	public ChargeProfile ChargeProfiles;
	public MitigatedBidSegment MitigatedBidSegment;
	public EnergyMarket EnergyMarket;
	public MarketParticipant MarketParticipant;

	public Bid(){

	}
}//end Bid