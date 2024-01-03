package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Length;
import IEC61968.Common.Status;
import IEC61968.Work.WorkLocation;

/**
 * A logical part of the design (e.g., pole and all equipment on a pole). This
 * includes points and spans.
 * @updated 03-Jan-2024 12:55:02 PM
 */
public class DesignLocation extends WorkIdentifiedObject {

	/**
	 * The legth of the span from the previous pole to this pole.
	 */
	public Length spanLength;
	public Status status;
	public MiscCostItem MiscCostItems;
	public DesignLocationCU DesignLocationCUs;
	public Design Designs;
	public ConditionFactor ConditionFactors;
	public WorkLocation WorkLocations;

	public DesignLocation(){

	}
}//end DesignLocation