package IEC61968.InfIEC61968.InfWork;

import IEC61968.Work.WorkTask;

/**
 * A set of tasks is required to implement a design.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class OldWorkTask extends WorkTask {

	public LaborItem LaborItems;
	public OverheadCost OverheadCost;
	public QualificationRequirement QualificationRequirements;
	public MiscCostItem MiscCostItems;
	public Usage Usages;
	public ContractorItem ContractorItems;

	public OldWorkTask(){

	}
}//end OldWorkTask