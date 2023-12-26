package IEC62325.MarketManagement;

import IEC61968.Common.Document;

/**
 * Electronic document containing the information necessary to satisfy a given
 * business process set of requirements.
 * @author effantin-cyr
 * @version 1.0
 * @created 25-Dec-2023 8:48:37 PM
 */
public class MarketDocument extends Document {

	public MarketDocument SelfMarketDocument;
	public Period Period;
	public AttributeInstanceComponent AttributeInstanceComponent;
	public Domain Domain;

	public MarketDocument(){

	}
}//end MarketDocument