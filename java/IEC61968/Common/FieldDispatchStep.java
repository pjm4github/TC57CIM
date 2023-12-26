package IEC61968.Common;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;

/**
 * Details of the step in the field dispatch history.
 * @author marga
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class FieldDispatchStep {

	/**
	 * The status of one or more crews dispatched to perform field work at one or more
	 * work sites
	 */
	public CrewStatusKind dispatchStatus;
	/**
	 * The date and time at which the dispatch status occurred.
	 */
	public DateTime occurredDateTime;
	/**
	 * freeform comments related to the dispatch to perform field work.
	 */
	public String remarks;
	/**
	 * The sequence number of the field dispatch step within the field dispatch
	 * history.  Begins with 1 and increments up.
	 */
	public Integer sequenceNumber;

	public FieldDispatchStep(){

	}
}//end FieldDispatchStep