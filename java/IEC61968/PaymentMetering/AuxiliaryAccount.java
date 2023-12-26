package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;
import IEC61968.Common.Document;

/**
 * Variable and dynamic part of auxiliary agreement, generally representing the
 * current state of the account related to the outstanding balance defined in
 * auxiliary agreement.
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AuxiliaryAccount extends Document {

	/**
	 * The total amount currently remaining on this account that is required to be
	 * paid in order to settle the account to zero. This excludes any due amounts not
	 * yet paid.
	 */
	public Money balance;
	/**
	 * Current amounts now due for payment on this account.
	 */
	public Due due;
	/**
	 * Details of the last credit transaction performed on this account.
	 */
	public AccountMovement lastCredit;
	/**
	 * Details of the last debit transaction performed on this account.
	 */
	public AccountMovement lastDebit;
	/**
	 * The initial principle amount, with which this account was instantiated.
	 */
	public Money principleAmount;
	/**
	 * All payments against this account.
	 */
	public Transaction PaymentTransactions;
	/**
	 * All charges levied on this account.
	 */
	public Charge Charges;

	public AuxiliaryAccount(){

	}
}//end AuxiliaryAccount