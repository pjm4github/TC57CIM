package IEC61968.Work;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Hours;
import IEC61968.Assets.Asset;
import IEC61968.Common.Crew;

/**
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public class WorkTask extends BaseWork {

	/**
	 * Date and time work task was completed.
	 */
	public DateTime completedDateTime;
	/**
	 * Total contractor costs associated with the work task.
	 */
	public Money contractorCost;
	/**
	 * Estimated time of arrival, so that customer or police/fire department can be
	 * informed when the crew will arrive.
	 */
	public DateTime crewETA;
	/**
	 * Instructions for performing this task.
	 */
	public String instruction;
	/**
	 * Total labor costs associated with the work task.
	 */
	public Money laborCost;
	/**
	 * Hours of labor expended under work task.
	 */
	public Hours laborHours;
	/**
	 * Total material costs associated with the work task.
	 */
	public Money materiallCost;
	/**
	 * If specified, override schedule and perform this task in accordance with
	 * instructions specified here.
	 */
	public String schedOverride;
	/**
	 * Date and time work task was started.
	 */
	public DateTime startedDateTime;
	/**
	 * Kind of work.
	 */
	public WorkTaskKind taskKind;
	/**
	 * Total tool costs associated with the work task.
	 */
	public Money toolCost;
	public MaterialItem MaterialItems;
	/**
	 * Old asset replaced by this work task.
	 */
	public Asset OldAsset;
	/**
	 * All assets on which this non-replacement work task is performed.
	 */
	public Asset Assets;
	/**
	 * All crews participating in this work task.
	 */
	public Crew Crews;

	public WorkTask(){

	}
}//end WorkTask