package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.String;

/**
 * Details of a bank account.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class BankAccountDetail {

	/**
	 * Operational account reference number.
	 */
	public String accountNumber;
	/**
	 * Name of bank where account is held.
	 */
	public String bankName;
	/**
	 * Branch of bank where account is held.
	 */
	public String branchCode;
	/**
	 * National identity number (or equivalent) of account holder.
	 */
	public String holderID;
	/**
	 * Name of account holder.
	 */
	public String holderName;

	public BankAccountDetail(){

	}
}//end BankAccountDetail