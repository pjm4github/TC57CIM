package IEC61968.Work;


/**
 * Maintenance work task.  Costs associated with this are considered preventive
 * maintenance (PM) costs.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class MaintenanceWorkTask extends WorkTask {

	/**
	 * Kind of breaker maintenance performed by this maintenance work task.
	 */
	public BreakerMaintenanceKind breakerMaintenanceKind;
	/**
	 * Kind of transformer maintenance performed by this maintenance work task.
	 */
	public TransformerMaintenanceKind transformerMaintenanceKind;

	public MaintenanceWorkTask(){

	}
}//end MaintenanceWorkTask