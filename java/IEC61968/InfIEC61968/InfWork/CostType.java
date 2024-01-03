package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61968.Common.Status;

/**
 * A categorization for resources, often costs, in accounting transactions.
 * Examples include: material components, building in service, coal sales,
 * overhead, etc.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CostType extends WorkIdentifiedObject {

	/**
	 * True if an amount can be assigned to the resource element (e.g., building in
	 * service, transmission plant, software development capital); false otherwise (e.
	 * g., internal labor, material components).
	 */
	public Boolean amountAssignable;
	/**
	 * A codified representation of the resource element.
	 */
	public String code;
	/**
	 * The level of the resource element in the hierarchy of resource elements
	 * (recursive relationship).
	 */
	public String level;
	/**
	 * The stage for which this costType applies: estimated design, estimated actual
	 * or actual actual. 
	 */
	public String stage;
	public Status status;
	public CostType ChildCostTypes;
	public WorkCostDetail WorkCostDetails;
	public ErpJournalEntry ErpJournalEntries;
	public CompatibleUnit CompatibleUnits;

	public CostType(){

	}
}//end CostType