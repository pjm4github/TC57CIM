package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ParticipantInterfaces.TransactionBid;
import IEC62325.MarketOperations.ParticipantInterfaces.Trade;
import IEC62325.MarketOperations.MarketSystem.MarketResults.ExPostPricingResults;
import IEC62325.MarketOperations.MarketSystem.MarketResults.PnodeResults;
import IEC62325.MarketOperations.MarketOpCommon.MktMeasurement;
import IEC62325.MarketOperations.CongestionRevenueRights.CRRSegment;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * A pricing node is directly associated with a connectivity node.  It is a
 * pricing location for which market participants submit their bids, offers,
 * buy/sell CRRs, and settle.
 * @created 28-Dec-2023 12:19:18 PM
 */
public class Pnode extends IdentifiedObject {

	/**
	 * If true, this Pnode is public (prices are published for DA/RT and FTR markets),
	 * otherwise it is private (location is not usable by market for
	 * bidding/FTRs/transactions).
	 */
	public Boolean isPublic;
	public SubControlArea SubControlArea;
	public TransactionBid ReceiptTransactionBids;
	public TransactionBid DeliveryTransactionBids;
	public Trade Trade;
	public ExPostPricingResults ExPostResults;
	public PnodeResults PnodeResults;
	/**
	 * Allows Measurements to be associated to Pnodes.
	 */
	public MktMeasurement MktMeasurement;
	public CRRSegment SourceCRRSegment;
	public CRRSegment SinkCRRSegment;
	/**
	 * A registered resource injects power at one or more connectivity nodes related
	 * to a pnode
	 */
	public RegisteredResource RegisteredResources;

	public Pnode(){

	}
}//end Pnode