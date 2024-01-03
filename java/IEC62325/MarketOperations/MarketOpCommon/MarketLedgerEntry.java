package IEC62325.MarketOperations.MarketOpCommon;

import IEC61970.Base.Domain.String;
import IEC62325.MarketOperations.MktDomain.MktAccountKind;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.Status;
import IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement;

/**
 * Details of an individual entry in a ledger, which was posted from a journal on
 * the posted date.
 * @created 03-Jan-2024 2:03:20 PM
 */
public class MarketLedgerEntry {

	/**
	 * Account identifier for this entry.
	 */
	public String accountID;
	/**
	 * Kind of account for this entry.
	 */
	public MktAccountKind accountKind;
	/**
	 * The amount of the debit or credit for this account.
	 */
	public Money amount;
	/**
	 * Date and time this entry was posted to the ledger.
	 */
	public DateTime postedDateTime;
	/**
	 * Status of ledger entry.
	 */
	public Status status;
	/**
	 * Date and time journal entry was recorded.
	 */
	public DateTime transactionDateTime;
	public Settlement Settlement;

	public MarketLedgerEntry(){

	}
}//end MarketLedgerEntry