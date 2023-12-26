package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Boolean;

/**
 * The operating shift for a vendor during which the vendor may transact against
 * the merchant's account. It aggregates transactions and receipts during the
 * shift and periodically debits a merchant account. The totals in vendor shift
 * should always be the sum of totals aggregated in all cashier shifts that were
 * open under the particular vendor shift.
 * @created 25-Dec-2023 8:45:26 PM
 */
public class VendorShift extends Shift {

	/**
	 * The amount that is to be debited from the merchant account for this vendor
	 * shift. This amount reflects the sum(PaymentTransaction.transactionAmount).
	 */
	public Money merchantDebitAmount;
	/**
	 * If true, merchantDebitAmount has been debited from MerchantAccount; typically
	 * happens at the end of VendorShift when it closes.
	 */
	public Boolean posted;
	/**
	 * All receipts recorded during this vendor shift.
	 */
	public Receipt Receipts;
	/**
	 * All transactions recorded during this vendor shift.
	 */
	public Transaction Transactions;

	public VendorShift(){

	}
}//end VendorShift