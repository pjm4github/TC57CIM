package IEC61968.Customers;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * Notifications for move-in, move-out, delinquencies, etc.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:18 PM
 */
public class AccountNotification {

	public String customerNotificationType;
	public String methodType;
	public String note;
	public DateTime time;

	public AccountNotification(){

	}
}//end AccountNotification