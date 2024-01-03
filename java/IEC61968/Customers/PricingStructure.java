package IEC61968.Customers;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61968.Metering.UsagePoint;
import IEC61968.PaymentMetering.Transaction;
import IEC61968.Common.Document;

/**
 * Grouping of pricing components and prices used in the creation of customer
 * charges and the eligibility criteria under which these terms may be offered to
 * a customer. The reasons for grouping include state, customer classification,
 * site characteristics, classification (i.e. fee price structure, deposit price
 * structure, electric service price structure, etc.) and accounting requirements.
 * @created 03-Jan-2024 12:17:34 PM
 */
public class PricingStructure extends Document {

	/**
	 * Unique user-allocated key for this pricing structure, used by company
	 * representatives to identify the correct price structure for allocating to a
	 * customer. For rate schedules it is often prefixed by a state code.
	 */
	public String code;
	/**
	 * Absolute maximum valid non-demand usage quantity used in validating a
	 * customer's billed non-demand usage.
	 */
	public Integer dailyCeilingUsage;
	/**
	 * Used in place of actual computed estimated average when history of usage is not
	 * available, and typically manually entered by customer accounting.
	 */
	public Integer dailyEstimatedUsage;
	/**
	 * Absolute minimum valid non-demand usage quantity used in validating a
	 * customer's billed non-demand usage.
	 */
	public Integer dailyFloorUsage;
	/**
	 * (accounting) Kind of revenue, often used to determine the grace period allowed,
	 * before collection actions are taken on a customer (grace periods vary between
	 * revenue classes).
	 */
	public RevenueKind revenueKind;
	/**
	 * True if this pricing structure is not taxable.
	 */
	public Boolean taxExemption;
	/**
	 * All service delivery points (with prepayment meter running as a stand-alone
	 * device, with no CustomerAgreement or Customer) to which this pricing structure
	 * applies.
	 */
	public UsagePoint UsagePoints;
	/**
	 * All transactions applying this pricing structure.
	 */
	public Transaction Transactions;
	/**
	 * All tariffs used by this pricing structure.
	 */
	public Tariff Tariffs;

	public PricingStructure(){

	}
}//end PricingStructure