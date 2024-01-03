package IEC61968.InfIEC61968.InfCommon;

import IEC61970.Base.Domain.String;
import IEC61968.Common.Document;

/**
 * Bank account.
 * @author T. Kostic
 * @version 1.0
 * @created 03-Jan-2024 12:32:56 PM
 */
public class BankAccount extends Document {

	/**
	 * Account reference number.
	 */
	public String accountNumber;
	/**
	 * Bank that provides this BankAccount.
	 */
	public Bank Bank;

	public BankAccount(){

	}
}//end BankAccount