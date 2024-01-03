package IEC62325.MarketOperations.MarketPlan;

import IEC61970.Base.Domain.String;

/**
 * Model that describes the Congestion Revenue Rights Auction Market.
 * @created 28-Dec-2023 8:11:21 PM
 */
public class CRRMarket extends Market {

	/**
	 * labelID - an ID for a set of apnodes/pnodes used in a CRR market
	 */
	public String labelID;

	public CRRMarket(){

	}
}//end CRRMarket