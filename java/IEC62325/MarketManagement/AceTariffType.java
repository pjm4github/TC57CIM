package IEC62325.MarketManagement;

import IEC61970.Base.Domain.String;

/**
 * The Area Control Error tariff type that is applied or used.
 * @author mspivbe2
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class AceTariffType {

	/**
	 * The coded type of an ACE tariff.
	 */
	public String type;
	public Unit Unit;
	public MarketDocument MarketDocument;

	public AceTariffType(){

	}
}//end AceTariffType