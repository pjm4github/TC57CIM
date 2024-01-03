package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.IntegerQuantity;
import IEC61970.Base.Domain.Date;
import IEC61968.Common.Status;
import IEC61970.Base.Domain.Boolean;

/**
 * Compatible unit at a given design location.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class DesignLocationCU extends WorkIdentifiedObject {

	/**
	 * A code that helps direct accounting (capital, expense, or accounting treatment).
	 */
	public String cuAccount;
	/**
	 * A code that instructs the crew what action to perform.
	 */
	public WorkActionKind cuAction;
	/**
	 * The quantity of the CU being assigned to this location.
	 */
	public IntegerQuantity cuQuantity;
	/**
	 * As the same CU can be used for different purposes and accounting purposes,
	 * usage must be specified. Examples include: distribution, transmission,
	 * substation.
	 */
	public String cuUsage;
	/**
	 * Year when a CU that represents an asset is removed.
	 */
	public Date removalDate;
	public Status status;
	/**
	 * True if associated electrical equipment is intended to be energized while work
	 * is being performed.
	 */
	public Boolean toBeEnergised;
	public CUGroup CUGroups;
	public Design Designs;
	public OldWorkTask WorkTasks;
	public ConditionFactor ConditionFactors;

	public DesignLocationCU(){

	}
}//end DesignLocationCU