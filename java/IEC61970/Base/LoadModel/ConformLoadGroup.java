package IEC61970.Base.LoadModel;


/**
 * A group of loads conforming to an allocation pattern.
 * @created 02-Jan-2024 11:11:31 PM
 */
public class ConformLoadGroup extends LoadGroup {

	/**
	 * Conform loads assigned to this ConformLoadGroup.
	 */
	public ConformLoad EnergyConsumers;
	/**
	 * The ConformLoadSchedules in the ConformLoadGroup.
	 */
	public ConformLoadSchedule ConformLoadSchedules;

	public ConformLoadGroup(){

	}
}//end ConformLoadGroup