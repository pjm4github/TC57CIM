import IEC61968.Common.Status;

/**
 * Individual entry of a given Ledger Budget, typically containing information
 * such as amount, accounting date, accounting period, and is associated with the
 * applicable general ledger account.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpLedBudLineItem extends ErpIdentifiedObject {

	public Status status;
	public ErpLedgerBudget ErpLedgerBudget;

	public ErpLedBudLineItem(){

	}
}//end ErpLedBudLineItem