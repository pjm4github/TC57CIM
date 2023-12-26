package IEC61968.Work;

import IEC61970.Base.Domain.Boolean;

/**
 * Work task for asset repair. Costs associated with this are considered
 * corrective maintenance (CM) costs.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public class RepairWorkTask extends WorkTask {

	/**
	 * Repair work is emergency.
	 */
	public Boolean emergency;

	public RepairWorkTask(){

	}
}//end RepairWorkTask