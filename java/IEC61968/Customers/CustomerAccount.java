package IEC61968.Customers;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61968.InfIEC61968.InfCustomers.WorkBillingInfo;
import IEC61968.PaymentMetering.Transaction;
import IEC61968.Common.Document;

/**
 * Assignment of a group of products and services purchased by the customer
 * through a customer agreement, used as a mechanism for customer billing and
 * payment. It contains common information from the various types of customer
 * agreements to create billings (invoices) for a customer and receive payment.
 * @created 03-Jan-2024 12:16:56 PM
 */
public class CustomerAccount extends Document {

	/**
	 * Cycle day on which the associated customer account will normally be billed,
	 * used to determine when to produce the billing.
	 */
	public String billingCycle;
	/**
	 * Budget bill code.
	 */
	public String budgetBill;
	/**
	 * The last amount that will be billed to the customer prior to shut off of the
	 * account.
	 */
	public Money lastBillAmount;
	public ErpInvoice ErpInvoicees;
	public WorkBillingInfo WorkBillingInfos;
	/**
	 * All payment transactions for this customer account.
	 */
	public Transaction PaymentTransactions;
	public AccountNotification AccountNotification;
	/**
	 * All agreements for this customer account.
	 */
	public CustomerAgreement CustomerAgreements;

	public CustomerAccount(){

	}
}//end CustomerAccount