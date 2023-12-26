import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Status;
import IEC61968.Common.UserAttribute;

/**
 * Details of an individual entry in a ledger, which was posted from a journal on
 * the posted date.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpLedgerEntry extends ErpIdentifiedObject {

	/**
	 * Account identifier for this entry.
	 */
	public String accountID;
	/**
	 * Kind of account for this entry.
	 */
	public ErpAccountKind accountKind;
	/**
	 * The amount of the debit or credit for this account.
	 */
	public Money amount;
	/**
	 * Date and time this entry was posted to the ledger.
	 */
	public DateTime postedDateTime;
	public Status status;
	/**
	 * Date and time journal entry was recorded.
	 */
	public DateTime transactionDateTime;
	public ErpJournalEntry ErpJounalEntry;
	public ErpLedBudLineItem ErpLedgerEntry;
	public UserAttribute UserAttributes;

	public ErpLedgerEntry(){

	}
}//end ErpLedgerEntry