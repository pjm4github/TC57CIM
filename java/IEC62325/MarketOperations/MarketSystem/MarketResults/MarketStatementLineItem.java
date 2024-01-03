package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute;

/**
 * An individual line item on an ISO settlement statement.
 * @created 28-Dec-2023 8:23:32 PM
 */
public class MarketStatementLineItem extends IdentifiedObject {

	/**
	 * Current settlement amount.
	 */
	public Float currentAmount;
	/**
	 * Current ISO settlement amount.
	 */
	public Float currentISOAmount;
	/**
	 * Current ISO settlement quantity. 
	 */
	public Float currentISOQuantity;
	/**
	 * Current settlement price.
	 */
	public Float currentPrice;
	/**
	 * Current settlement quantity, subject to the UOM. 
	 */
	public Float currentQuantity;
	/**
	 * The date of which the settlement is run.
	 */
	public DateTime intervalDate;
	/**
	 * The number of intervals. 
	 */
	public String intervalNumber;
	/**
	 * Net settlement amount.
	 */
	public Float netAmount;
	/**
	 * Net ISO settlement amount.
	 */
	public Float netISOAmount;
	/**
	 * Net ISO settlement quantity. 
	 */
	public Float netISOQuantity;
	/**
	 * Net settlement price.
	 */
	public Float netPrice;
	/**
	 * Net settlement quantity, subject to the UOM. 
	 */
	public Float netQuantity;
	/**
	 * Previous settlement amount.
	 */
	public Float previousAmount;
	/**
	 * Previous ISO settlement amount.
	 */
	public Float previousISOAmount;
	/**
	 * Previous ISO settlement quantity. 
	 */
	public Float previousISOQuantity;
	/**
	 * Previous settlement price.
	 */
	public Float previousPrice;
	/**
	 * Previous settlement quantity, subject to the UOM. 
	 */
	public Float previousQuantity;
	/**
	 * The unit of measure for the quantity element of the line item. 
	 */
	public String quantityUOM;
	public MarketStatementLineItem ContainerMarketStatementLineItem;
	public MarketStatement MarketStatement;
	public MktUserAttribute MktUserAttribute;

	public MarketStatementLineItem(){

	}
}//end MarketStatementLineItem