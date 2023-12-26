///////////////////////////////////////////////////////////
//  PricingStructure.h
//  Implementation of the Class PricingStructure
//  Created on:      25-Dec-2023 8:45:24 PM
///////////////////////////////////////////////////////////

#if !defined(EA_4DE13F6E_7BE5_42cb_BA9A_011EAFE31497__INCLUDED_)
#define EA_4DE13F6E_7BE5_42cb_BA9A_011EAFE31497__INCLUDED_

#include "String.h"
#include "Integer.h"
#include "IEC61968\Customers\RevenueKind.java"
#include "Boolean.h"
#include "UsagePoint.h"
#include "IEC61968\PaymentMetering\Transaction.java"
#include "Tariff.h"
#include "Document.h"

/**
 * Grouping of pricing components and prices used in the creation of customer
 * charges and the eligibility criteria under which these terms may be offered to
 * a customer. The reasons for grouping include state, customer classification,
 * site characteristics, classification (i.e. fee price structure, deposit price
 * structure, electric service price structure, etc.) and accounting requirements.
 */
class PricingStructure : public Document
{

public:
	PricingStructure();
	/**
	 * Unique user-allocated key for this pricing structure, used by company
	 * representatives to identify the correct price structure for allocating to a
	 * customer. For rate schedules it is often prefixed by a state code.
	 */
	String code;
	/**
	 * Absolute maximum valid non-demand usage quantity used in validating a
	 * customer's billed non-demand usage.
	 */
	Integer dailyCeilingUsage;
	/**
	 * Used in place of actual computed estimated average when history of usage is not
	 * available, and typically manually entered by customer accounting.
	 */
	Integer dailyEstimatedUsage;
	/**
	 * Absolute minimum valid non-demand usage quantity used in validating a
	 * customer's billed non-demand usage.
	 */
	Integer dailyFloorUsage;
	/**
	 * (accounting) Kind of revenue, often used to determine the grace period allowed,
	 * before collection actions are taken on a customer (grace periods vary between
	 * revenue classes).
	 */
	RevenueKind revenueKind;
	/**
	 * True if this pricing structure is not taxable.
	 */
	Boolean taxExemption;
	/**
	 * All service delivery points (with prepayment meter running as a stand-alone
	 * device, with no CustomerAgreement or Customer) to which this pricing structure
	 * applies.
	 */
	UsagePoint *UsagePoints;
	/**
	 * All transactions applying this pricing structure.
	 */
	Transaction *Transactions;
	/**
	 * All tariffs used by this pricing structure.
	 */
	Tariff *Tariffs;

};
#endif // !defined(EA_4DE13F6E_7BE5_42cb_BA9A_011EAFE31497__INCLUDED_)
