///////////////////////////////////////////////////////////
//  CustomerAccount.h
//  Implementation of the Class CustomerAccount
//  Created on:      25-Dec-2023 8:45:20 PM
///////////////////////////////////////////////////////////

#if !defined(EA_23C24A0B_2CFB_4af0_8275_2C3F8DCF1A19__INCLUDED_)
#define EA_23C24A0B_2CFB_4af0_8275_2C3F8DCF1A19__INCLUDED_

#include "String.h"
#include "Money.py"
#include "\ErpInvoice.java"
#include "WorkBillingInfo.h"
#include "IEC61968\PaymentMetering\Transaction.java"
#include "IEC61968\Customers\AccountNotification.java"
#include "CustomerAgreement.h"
#include "Document.h"

/**
 * Assignment of a group of products and services purchased by the customer
 * through a customer agreement, used as a mechanism for customer billing and
 * payment. It contains common information from the various types of customer
 * agreements to create billings (invoices) for a customer and receive payment.
 */
class CustomerAccount : public Document
{

public:
	CustomerAccount();
	/**
	 * Cycle day on which the associated customer account will normally be billed,
	 * used to determine when to produce the billing.
	 */
	String billingCycle;
	/**
	 * Budget bill code.
	 */
	String budgetBill;
	/**
	 * The last amount that will be billed to the customer prior to shut off of the
	 * account.
	 */
	Money lastBillAmount;
	ErpInvoice *ErpInvoicees;
	WorkBillingInfo *WorkBillingInfos;
	/**
	 * All payment transactions for this customer account.
	 */
	Transaction *PaymentTransactions;
	AccountNotification *AccountNotification;
	/**
	 * All agreements for this customer account.
	 */
	CustomerAgreement *CustomerAgreements;

};
#endif // !defined(EA_23C24A0B_2CFB_4af0_8275_2C3F8DCF1A19__INCLUDED_)
