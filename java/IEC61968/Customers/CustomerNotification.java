package IEC61968.Customers;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * Conditions for notifying the customer about the changes in the status of their
 * service (e.g., outage restore, estimated restoration time, tariff or service
 * level change, etc.)
 * @author T. Kostic
 * @version 1.0
 * @created 03-Jan-2024 12:17:18 PM
 */
public class CustomerNotification {

	/**
	 * Type of contact (e.g., phone, email, etc.).
	 */
	public String contactType;
	/**
	 * Value of contact type (e.g., phone number, email address, etc.).
	 */
	public String contactValue;
	/**
	 * Earliest date time to call the customer.
	 */
	public DateTime earliestDateTimeToCall;
	/**
	 * Latest date time to call the customer.
	 */
	public DateTime latestDateTimeToCall;
	/**
	 * Trigger for this notification.
	 */
	public NotificationTriggerKind trigger;
	/**
	 * Customer requiring this notification.
	 */
	public Customer Customer;
	/**
	 * All trouble tickets with this notification.
	 */
	public TroubleTicket TroubleTickets;

	public CustomerNotification(){

	}
}//end CustomerNotification