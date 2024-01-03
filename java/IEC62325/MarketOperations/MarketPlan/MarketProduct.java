package IEC62325.MarketOperations.MarketPlan;

import IEC62325.MarketOperations.MktDomain.MarketProductType;
import IEC61970.Base.Domain.Float;
import IEC62325.MarketOperations.ParticipantInterfaces.ProductBid;
import IEC62325.MarketOperations.MarketSystem.MarketResults.ResourceAwardInstruction;
import IEC62325.MarketOperations.ParticipantInterfaces.BidError;
import IEC62325.MarketOperations.ReferenceData.BidPriceCap;
import IEC62325.MarketOperations.MarketSystem.MarketResults.MarketRegionResults;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A product traded by an RTO (e.g. energy, 10 minute spinning reserve).
 * Ancillary service product examples include: Regulation, Regulation Up,
 * Regulation Down, Spinning Reserve, Non-Spinning Reserve, etc.
 * @created 03-Jan-2024 2:06:41 PM
 */
public class MarketProduct extends IdentifiedObject {

	/**
	 * Market product type examples:
	 * 
	 * EN (Energy)
	 * RU (Regulation Up)
	 * RD (Regulation Dn)
	 * SR (Spinning Reserve)
	 * NR (Non-Spinning Reserve)
	 * RC (RUC)
	 */
	public MarketProductType marketProductType;
	/**
	 * Ramping time interval for the specific market product type specified by
	 * marketProductType attribute. For example, if marketProductType = EN (from
	 * enumeration MarketProductType), then the rampInterval is the ramping time
	 * interval for Energy.
	 */
	public Float rampInterval;
	public ProductBid ProductBids;
	public ResourceAwardInstruction ResourceAwardInstruction;
	public BidError BidError;
	public BidPriceCap BidPriceCap;
	public MarketRegionResults MarketRegionResults;
	public Market Market;

	public MarketProduct(){

	}
}//end MarketProduct