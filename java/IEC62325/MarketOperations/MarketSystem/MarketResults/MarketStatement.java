package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61968.Common.Document;

/**
 * A statement is a roll up of statement line items. Each statement along with its
 * line items provide the details of specific charges at any given time.  Used by
 * Billing and Settlement.
 * @created 28-Dec-2023 8:23:22 PM
 */
public class MarketStatement extends Document {

	/**
	 * The end of a bill period.
	 */
	public DateTime end;
	/**
	 * The version number of previous statement (in the case of true up).
	 */
	public String referenceNumber;
	/**
	 * The start of a bill period.
	 */
	public DateTime start;
	/**
	 * The date of which Settlement is run.
	 */
	public DateTime tradeDate;
	/**
	 * The date of which this statement is issued. 
	 */
	public DateTime transactionDate;

	public MarketStatement(){

	}
}//end MarketStatement