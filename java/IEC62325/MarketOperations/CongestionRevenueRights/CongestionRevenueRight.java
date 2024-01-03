package IEC62325.MarketOperations.CongestionRevenueRights;

import IEC62325.MarketOperations.MktDomain.CRRCategoryType;
import IEC62325.MarketOperations.MktDomain.CRRSegmentType;
import IEC62325.MarketOperations.MktDomain.CRRHedgeType;
import IEC62325.MarketOperations.MktDomain.TimeOfUse;
import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.ReferenceData.Flowgate;
import IEC62325.MarketOperations.MarketPlan.CRRMarket;
import IEC61968.Common.Document;

/**
 * Congestion Revenue Rights (CRR) class that is inherited from a Document class.
 * 
 * A CRR is a financial concept that is used to hedge congestion charges.
 * 
 * The CRR is usually settled based on the Locational Marginal Prices (LMPs) that
 * are calculated in the day-ahead market. These LMPs are determined by the Day-
 * ahead resource schedules/bids. CRRs will not hedge against marginal losses. If
 * the congestion component of LMP at the sink is greater than at the source, then
 * the CRR owner is entitled to receive a portion of congestion revenues. If the
 * congestion component at the sink is less than at the source, then an obligation-
 * type CRR owner will be charged, but an option-type CRR owner will not.
 * @created 03-Jan-2024 2:02:21 PM
 */
public class CongestionRevenueRight extends Document {

	/**
	 * CRR category represents 'PTP' for a point-to-point CRR, or 'NSR' for a Network
	 * Service Right. If CRR category is 'PTP', both Source ID and Sink ID fields are
	 * required. If CRR category is 'NSR' only one field, either Source ID or Sink ID,
	 * shall be not null and the other shall be null. However, the 'NSR' category will
	 * include at least three records.
	 */
	public CRRCategoryType cRRcategory;
	/**
	 * Type of the CRR, from the possible type definitions in the CRR System (e.g.
	 * 'LSE', 'ETC').
	 */
	public CRRSegmentType cRRtype;
	/**
	 * Hedge type Obligation or Option. An obligation type requires the holder to
	 * receive or pay the congestion rent. An option type gives the holder the option
	 * of receiving or paying the congestion rent.
	 */
	public CRRHedgeType hedgeType;
	/**
	 * Time of Use flag of the CRR - Peak (ON), Offpeak (OFF) or all 24 hours (24HR).
	 */
	public TimeOfUse timeOfUse;
	/**
	 * Segment of the CRR described in the current record.
	 */
	public String tradeSliceID;
	public Flowgate Flowgate;
	public CRRMarket CRRMarket;
	public CRRSegment CRRSegment;

	public CongestionRevenueRight(){

	}
}//end CongestionRevenueRight