package IEC62325.InfIEC62325.InfCongestionRevenueRights;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.ActivePower;
import IEC61968.Common.Agreement;
import IEC62325.MarketOperations.ReferenceData.Pnode;

/**
 * Financial Transmission Rights (FTR) regarding transmission capacity at a
 * flowgate.
 * @created 02-Jan-2024 11:58:01 PM
 */
public class FTR extends Agreement {

	/**
	 * Buy, Sell
	 */
	public String action;
	/**
	 * Quantity, typically MWs - Seller owns all rights being offered, MWs over time
	 * on same Point of Receipt, Point of Delivery, or Resource.
	 */
	public ActivePower baseEnergy;
	/**
	 * Peak, Off-peak, 24-hour
	 */
	public String class;
	/**
	 * Type of rights being offered (product) allowed to be auctioned (option,
	 * obligation).
	 */
	public String ftrType;
	/**
	 * Fixed (covers re-configuration, grandfathering) or Optimized (up for
	 * sale/purchase
	 */
	public String optimized;
	public Pnode Pnodes;

	public FTR(){

	}
}//end FTR