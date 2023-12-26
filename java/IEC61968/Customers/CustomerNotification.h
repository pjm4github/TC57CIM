///////////////////////////////////////////////////////////
//  CustomerNotification.h
//  Implementation of the Class CustomerNotification
//  Created on:      25-Dec-2023 8:45:20 PM
//  Original author: T. Kostic
///////////////////////////////////////////////////////////

#if !defined(EA_D9C86837_472D_457b_9274_594EECF564E3__INCLUDED_)
#define EA_D9C86837_472D_457b_9274_594EECF564E3__INCLUDED_

#include "String.h"
#include "DateTime.py"
#include "IEC61968\Customers\NotificationTriggerKind.java"
#include "Customer.h"
#include "TroubleTicket.h"

/**
 * Conditions for notifying the customer about the changes in the status of their
 * service (e.g., outage restore, estimated restoration time, tariff or service
 * level change, etc.)
 */
class CustomerNotification
{

public:
	CustomerNotification();
	/**
	 * Type of contact (e.g., phone, email, etc.).
	 */
	String contactType;
	/**
	 * Value of contact type (e.g., phone number, email address, etc.).
	 */
	String contactValue;
	/**
	 * Earliest date time to call the customer.
	 */
	DateTime earliestDateTimeToCall;
	/**
	 * Latest date time to call the customer.
	 */
	DateTime latestDateTimeToCall;
	/**
	 * Trigger for this notification.
	 */
	NotificationTriggerKind trigger;
	/**
	 * Customer requiring this notification.
	 */
	Customer *Customer;
	/**
	 * All trouble tickets with this notification.
	 */
	TroubleTicket *TroubleTickets;

};
#endif // !defined(EA_D9C86837_472D_457b_9274_594EECF564E3__INCLUDED_)
