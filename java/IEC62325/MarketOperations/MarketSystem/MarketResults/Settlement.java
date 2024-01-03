package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Document;

/**
 * Specifies a settlement run.
 * @created 03-Jan-2024 2:09:38 PM
 */
public class Settlement extends Document {

	/**
	 * The trade date on which the settlement is run. 
	 */
	public DateTime tradeDate;

	public Settlement(){

	}
}//end Settlement