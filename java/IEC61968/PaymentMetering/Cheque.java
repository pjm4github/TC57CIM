package IEC61968.PaymentMetering;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Date;

/**
 * The actual tender when it is a type of cheque.
 * @created 25-Dec-2023 8:45:20 PM
 */
public class Cheque {

	/**
	 * Details of the account holder and bank.
	 */
	public BankAccountDetail bankAccountDetail;
	/**
	 * Cheque reference number as printed on the cheque.
	 */
	public String chequeNumber;
	/**
	 * Date when cheque becomes valid.
	 */
	public Date date;
	/**
	 * Kind of cheque.
	 */
	public ChequeKind kind;
	/**
	 * The magnetic ink character recognition number printed on the cheque.
	 */
	public String micrNumber;
	/**
	 * Payment tender the cheque is being used for.
	 */
	public Tender Tender;

	public Cheque(){

	}
}//end Cheque