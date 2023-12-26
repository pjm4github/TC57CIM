package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.Money;

/**
 * The operating shift for a cashier, during which the cashier may transact
 * against the cashier shift, subject to vendor shift being open.
 * @created 25-Dec-2023 8:45:20 PM
 */
public class CashierShift extends Shift {

	/**
	 * The amount of cash that the cashier brings to start the shift and that will be
	 * taken away at the end of the shift; i.e. the cash float does not get banked.
	 */
	public Money cashFloat;
	/**
	 * All Receipts recorded for this Shift.
	 */
	public Receipt Receipts;
	/**
	 * Point of sale that is in operation during this shift.
	 */
	public PointOfSale PointOfSale;
	/**
	 * All transactions recorded during this cashier shift.
	 */
	public Transaction Transactions;

	public CashierShift(){

	}
}//end CashierShift