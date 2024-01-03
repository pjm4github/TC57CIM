package IEC62325.MarketOperations.MarketSystem.MarketResults;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.FloatQuantity;
import IEC61968.Common.Document;
import IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute;

/**
 * Pass Through Bill is used for:
 * 1)Two sided charge transactions with or without ISO involvement
 * 2) Specific direct charges or payments that are calculated outside or provided
 * directly to settlements
 * 3) Specific charge bill determinants that are externally supplied and used in
 * charge calculations
 * @created 28-Dec-2023 8:24:12 PM
 */
public class PassThroughBill extends Document {

	public Money adjustedAmount;
	/**
	 * The charge amount of the product/service.
	 */
	public Money amount;
	/**
	 * The company to which the PTB transaction is billed.
	 */
	public String billedTo;
	/**
	 * Bill period end date
	 */
	public DateTime billEnd;
	/**
	 * The settlement run type, for example: prelim, final, and rerun.
	 */
	public String billRunType;
	/**
	 * Bill period start date
	 */
	public DateTime billStart;
	/**
	 * The effective date of the transaction
	 */
	public DateTime effectiveDate;
	/**
	 * Disputed transaction indicator 
	 */
	public Boolean isDisputed;
	/**
	 * A flag indicating whether there is a profile data associated with the PTB.
	 */
	public Boolean isProfiled;
	/**
	 * The company to which the PTB transaction is paid.
	 */
	public String paidTo;
	/**
	 * The previous bill period end date
	 */
	public DateTime previousEnd;
	/**
	 * The previous bill period start date
	 */
	public DateTime previousStart;
	/**
	 * The price of product/service.
	 */
	public Money price;
	/**
	 * The product identifier for determining the charge type of the transaction. 
	 */
	public String productCode;
	/**
	 * The company by which the PTB transaction service is provided.
	 */
	public String providedBy;
	/**
	 * The product quantity.
	 */
	public FloatQuantity quantity;
	/**
	 * The end date of service provided, if periodic.
	 */
	public DateTime serviceEnd;
	/**
	 * The start date of service provided, if periodic. 
	 */
	public DateTime serviceStart;
	/**
	 * The company to which the PTB transaction is sold.
	 */
	public String soldTo;
	/**
	 * The tax on services taken.
	 */
	public Money taxAmount;
	/**
	 * The time zone code
	 */
	public String timeZone;
	/**
	 * The trade date
	 */
	public DateTime tradeDate;
	/**
	 * The date the transaction occurs.
	 */
	public DateTime transactionDate;
	/**
	 * The type of transaction. For example, charge customer, bill customer, matching
	 * AR/AP, or bill determinant 
	 */
	public String transactionType;
	public MarketStatementLineItem MarketStatementLineItem;
	public MktUserAttribute MktUserAttribute;

	public PassThroughBill(){

	}
}//end PassThroughBill