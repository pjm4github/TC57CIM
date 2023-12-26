package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;
import IEC61968.Common.Document;

/**
 * The operating account controlled by merchant agreement, against which the
 * vendor may vend tokens or receipt payments. Transactions via vendor shift debit
 * the account and bank deposits via bank statement credit the account.
 * @created 25-Dec-2023 8:45:22 PM
 */
public class MerchantAccount extends Document {

	/**
	 * The current operating balance of this account.
	 */
	public Money currentBalance;
	/**
	 * The balance of this account after taking into account any pending debits from
	 * VendorShift.merchantDebitAmount and pending credits from BankStatement.
	 * merchantCreditAmount or credits (see also BankStatement attributes and
	 * VendorShift attributes).
	 */
	public Money provisionalBalance;
	/**
	 * All transactors this merchant account is registered with.
	 */
	public Transactor Transactors;
	/**
	 * All vendor shifts that operate on this merchant account.
	 */
	public VendorShift VendorShifts;

	public MerchantAccount(){

	}
}//end MerchantAccount