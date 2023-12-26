import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Status;

/**
 * Details of an individual entry in a journal, which is to be posted to a ledger
 * on the posting date.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpJournalEntry extends ErpIdentifiedObject {

	/**
	 * Account identifier for this entry.
	 */
	public String accountID;
	/**
	 * The amount of the debit or credit for this account.
	 */
	public Money amount;
	/**
	 * Date and time this entry is to be posted to the ledger.
	 */
	public DateTime postingDateTime;
	/**
	 * The identifer of the source for this entry.
	 */
	public String sourceID;
	public Status status;
	/**
	 * Date and time journal entry was recorded.
	 */
	public DateTime transactionDateTime;

	public ErpJournalEntry(){

	}
}//end ErpJournalEntry