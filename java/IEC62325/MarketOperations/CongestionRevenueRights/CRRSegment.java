package IEC62325.MarketOperations.CongestionRevenueRights;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * CRRSegment represents a segment of a CRR in a particular time frame.
 * 
 * The segment class contains amount, clearing price, start date and time, end
 * date and time.
 * @created 03-Jan-2024 2:02:21 PM
 */
public class CRRSegment extends IdentifiedObject {

	/**
	 * Dollar amount = quantity x clearingPrice
	 */
	public Money amount;
	/**
	 * Clearing price of a CRR
	 */
	public Money clearingPrice;
	/**
	 * segment end date time
	 */
	public DateTime endDateTime;
	/**
	 * The MW amount associated with the CRR
	 */
	public Float quantity;
	/**
	 * segment start date time
	 */
	public DateTime startDateTime;

	public CRRSegment(){

	}
}//end CRRSegment