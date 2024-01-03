package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.CostPerEnergyUnit;
import IEC62325.MarketOperations.MktDomain.MarketType;

/**
 * This class represent the bid price cap.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class BidPriceCap {

	/**
	 * Bid Ceiling ($/MWH)
	 */
	public CostPerEnergyUnit bidCeiling;
	/**
	 * Bid Ceiling ($/MWH) for generic AS versus a specific market product
	 */
	public CostPerEnergyUnit bidCeilingAS;
	/**
	 * Bid Floor, ($/MWH)
	 */
	public CostPerEnergyUnit bidFloor;
	/**
	 * Bid Floor ($/MWH) for generic AS versus a specific market product
	 */
	public CostPerEnergyUnit bidFloorAS;
	/**
	 * Bid Default Price($/MWH)
	 */
	public CostPerEnergyUnit defaultPrice;
	/**
	 * Market Type of the cap (DAM or RTM)
	 */
	public MarketType marketType;

	public BidPriceCap(){

	}
}//end BidPriceCap