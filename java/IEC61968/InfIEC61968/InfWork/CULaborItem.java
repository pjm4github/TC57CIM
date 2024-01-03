package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Hours;
import IEC61970.Base.Domain.CostRate;
import IEC61968.Common.Status;

/**
 * Compatible unit labor item.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CULaborItem extends WorkIdentifiedObject {

	/**
	 * Activity code identifies a specific and distinguishable unit of work.
	 */
	public String activityCode;
	/**
	 * Estimated time to perform work.
	 */
	public Hours laborDuration;
	/**
	 * The labor rate applied for work.
	 */
	public CostRate laborRate;
	public Status status;
	public QualificationRequirement QualificationRequirements;
	public CULaborCode CULaborCode;
	public CompatibleUnit CompatibleUnits;

	public CULaborItem(){

	}
}//end CULaborItem