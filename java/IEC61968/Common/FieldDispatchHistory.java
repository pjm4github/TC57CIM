package IEC61968.Common;

import IEC61968.Operations.UnplannedOutage;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Operations.PlannedOutage;

/**
 * The history of field dispatch statuses for this work.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class FieldDispatchHistory extends IdentifiedObject {

	public UnplannedOutage UnplannedOutage;
	public PlannedOutage PlannedOutage;
	public Crew Crew;
	public FieldDispatchStep FieldDispatchStep;

	public FieldDispatchHistory(){

	}
}//end FieldDispatchHistory