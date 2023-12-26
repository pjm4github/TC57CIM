package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;

/**
 * Credit/debit movements for an account.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:18 PM
 */
public class AccountMovement {

	/**
	 * Amount that was credited to/debited from an account. For example: payment
	 * received/interest charge on arrears.
	 */
	public Money amount;
	/**
	 * Date and time when the credit/debit transaction was performed.
	 */
	public DateTime dateTime;
	/**
	 * Reason for credit/debit transaction on an account. Example: payment
	 * received/arrears interest levied.
	 */
	public String reason;

	public AccountMovement(){

	}
}//end AccountMovement