package IEC61968.InfIEC61968.InfCustomers;

import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.String;
import IEC61968.Customers.CustomerAccount;
import IEC61968.Common.Document;

/**
 * The creation of the monthly customer billing statements is the method employed
 * to notify Customers of charges, adjustments and credits applied to their
 * account for Services and Products. The actuall billing occurs through an
 * ErpInvoice. The CustomerBillingInfo includes information from the payment,
 * collection, meter reading, installed meter, service, site, customer, customer
 * account, customer agreement, services and pricing subject areas. Each component
 * price shows up as a separate line item on the ErpInvoice.
 * The Customer Billing Statement may include collection and account messages,
 * marketing/civic event messages and bill inserts.
 * One Customer Billing Statement is produced for all Agreements under a
 * CustomerAccount per billing cycle date defined in 'CustomerAccount.
 * billingCycle'.
 * The history of CustomerBillingInfo, Invoices and Payments is to be maintained
 * in associated ActivityRecords.
 * @created 29-Dec-2023 9:25:11 PM
 */
public class CustomerBillingInfo extends Document {

	/**
	 * Business date designated for the billing run which produced this
	 * CustomerBillingInfo. 
	 */
	public Date billingDate;
	/**
	 * Calculated date upon which a customer billing amount is due, used in the
	 * invoicing process to determine when a Customer's Payment is delinquent. It
	 * takes into consideration the regulatory criteria and the Customer's requested
	 * due date. In the absence of a Customer requested due date, the due date is
	 * typically calculated from the regulated number of days and the 'billingDate'.
	 */
	public Date dueDate;
	/**
	 * Kind of bill customer receives.
	 */
	public CustomerBillingKind kind;
	/**
	 * Amount of the last payment received from the customer. It is retained in the
	 * Customer Billing system, although the details of each payment are tracked in
	 * the ERP system.
	 */
	public Money lastPaymentAmt;
	/**
	 * Date of the last payment received from the customer. It is retained in the
	 * Customer Billing system, although the details of each payment are tracked in
	 * the ERP system.
	 */
	public Date lastPaymentDate;
	/**
	 * Outstanding balance on the CustomerAccount as of the statement date.
	 */
	public Money outBalance;
	/**
	 * Monthly amortized amount due during each billing cycle for the CustomerAccount
	 * balance for which the Payment Plan is set-up.
	 */
	public Money pymtPlanAmt;
	/**
	 * Type of payment plan.
	 */
	public String pymtPlanType;
	public ErpInvoiceLineItem ErpInvoiceLineItems;
	public CustomerAccount CustomerAccount;

	public CustomerBillingInfo(){

	}
}//end CustomerBillingInfo