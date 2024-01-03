package IEC61970.Base.LoadModel;


/**
 * Loads that do not follow a daily and seasonal load variation pattern.
 * @created 02-Jan-2024 11:13:14 PM
 */
public class NonConformLoadGroup extends LoadGroup {

	/**
	 * Conform loads assigned to this ConformLoadGroup.
	 */
	public NonConformLoad EnergyConsumers;
	/**
	 * The NonConformLoadSchedules in the NonConformLoadGroup.
	 */
	public NonConformLoadSchedule NonConformLoadSchedules;

	public NonConformLoadGroup(){

	}
}//end NonConformLoadGroup