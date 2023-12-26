package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.RealEnergy;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Metering.Meter;

/**
 * The record of details of payment for service or token sale.
 * @created 25-Dec-2023 8:45:25 PM
 */
public class Transaction extends IdentifiedObject {

	/**
	 * Formal reference for use with diverse payment (traffic fine for example).
	 */
	public String diverseReference;
	/**
	 * Reference to the entity that is the source of 'amount' (for example: customer
	 * for token purchase; or supplier for free issue token).
	 */
	public String donorReference;
	/**
	 * Kind of transaction.
	 */
	public TransactionKind kind;
	/**
	 * Transaction amount, rounding, date and note for this transaction line.
	 */
	public LineDetail line;
	/**
	 * Reference to the entity that is the recipient of 'amount' (for example,
	 * supplier for service charge payment; or tax receiver for VAT).
	 */
	public String receiverReference;
	/**
	 * (if 'kind' is transactionReversal) Reference to the original transaction that
	 * is being reversed by this transaction.
	 */
	public String reversedId;
	/**
	 * Actual amount of service units that is being paid for.
	 */
	public RealEnergy serviceUnitsEnergy;
	/**
	 * Number of service units not reflected in 'serviceUnitsEnergy' due to process
	 * rounding or truncating errors.
	 */
	public RealEnergy serviceUnitsError;
	/**
	 * Meter for this vending transaction.
	 */
	public Meter Meter;

	public Transaction(){

	}
}//end Transaction