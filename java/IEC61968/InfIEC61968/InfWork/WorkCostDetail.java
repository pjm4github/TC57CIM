package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Work.Work;

/**
 * A collection of all of the individual cost items collected from multiple
 * sources.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class WorkCostDetail extends WorkDocument {

	/**
	 * Amount in designated currency for work, either a total or an individual element.
	 * As defined in the attribute "type," multiple instances are applicable to each
	 * work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted
	 * cost, other.
	 */
	public Money amount;
	/**
	 * True if 'amount' is a debit, false if it is a credit.
	 */
	public Boolean isDebit;
	/**
	 * Date and time that 'amount' is posted to the work.
	 */
	public DateTime transactionDateTime;
	public ErpProjectAccounting ErpProjectAccounting;
	public ContractorItem ContractorItems;
	public WorkCostSummary WorkCostSummary;
	public PropertyUnit PropertyUnits;
	public OldWorkTask WorkTask;
	public Work Works;

	public WorkCostDetail(){

	}
}//end WorkCostDetail