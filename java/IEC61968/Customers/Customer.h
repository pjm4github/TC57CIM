///////////////////////////////////////////////////////////
//  Customer.h
//  Implementation of the Class Customer
//  Created on:      25-Dec-2023 8:45:20 PM
///////////////////////////////////////////////////////////

#if !defined(EA_C4C233C2_9568_441b_A339_36491D483390__INCLUDED_)
#define EA_C4C233C2_9568_441b_A339_36491D483390__INCLUDED_

#include "IEC61968\Customers\CustomerKind.java"
#include "String.h"
#include "IEC61968\Common\Priority.java"
#include "Status.py"
#include "Boolean.h"
#include "IEC61968\Metering\EndDevice.java"
#include "CustomerAccount.h"
#include "OldPerson.h"
#include "CustomerAgreement.h"
#include "Work.py"
#include "IEC61968\Operations\OutagePlan.java"
#include "OrganisationRole.py"

/**
 * Organisation receiving services from service supplier.
 */
class Customer : public OrganisationRole
{

public:
	Customer();
	/**
	 * Kind of customer.
	 */
	CustomerKind kind;
	/**
	 * Locale designating language to use in communications with this customer.
	 */
	String locale;
	/**
	 * Priority of the customer.
	 */
	Priority priority;
	/**
	 * (if applicable) Public utilities commission (PUC) identification number.
	 */
	String pucNumber;
	/**
	 * True if customer organisation has special service needs such as life support,
	 * hospitals, etc.
	 */
	String specialNeed;
	/**
	 * Status of this customer.
	 */
	Status status;
	/**
	 * (use 'priority' instead) True if this is an important customer. Importance is
	 * for matters different than those in 'specialNeed' attribute.
	 */
	Boolean vip;
	/**
	 * All end devices of this customer.
	 */
	EndDevice *EndDevices;
	Customer *Customer;
	/**
	 * All accounts of this customer.
	 */
	CustomerAccount *CustomerAccounts;
	OldPerson *ErpPersons;
	/**
	 * All agreements of this customer.
	 */
	CustomerAgreement *CustomerAgreements;
	/**
	 * All the works performed for this customer.
	 */
	Work *Works;
	/**
	 * The outage plan that identifies the customers that are affected.
	 */
	OutagePlan *OutagePlan;

};
#endif // !defined(EA_C4C233C2_9568_441b_A339_36491D483390__INCLUDED_)
