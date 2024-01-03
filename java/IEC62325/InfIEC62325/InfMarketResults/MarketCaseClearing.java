package IEC62325.InfIEC62325.InfMarketResults;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC62325.MarketOperations.MarketPlan.MarketFactors;

/**
 * Market case clearing results are posted for a given settlement period.
 * @created 03-Jan-2024 1:54:12 PM
 */
public class MarketCaseClearing extends MarketFactors {

	/**
	 * Settlement period:
	 * 'DA - Bid-in'
	 * 'DA - Reliability'
	 * 'DA - Amp1'
	 * 'DA - Amp2'
	 * 'RT - Ex-Ante'
	 * 'RT - Ex-Post'
	 * 'RT - Amp1'
	 * 'RT - Amp2'
	 */
	public String caseType;
	/**
	 * Last time and date clearing results were manually modified.
	 */
	public DateTime modifiedDate;
	/**
	 * Bid clearing results posted time and date.
	 */
	public DateTime postedDate;

	public MarketCaseClearing(){

	}
}//end MarketCaseClearing