package IEC61968.Common;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Faults.FaultCauseType;

/**
 * Used to report details on creation, change or deletion of an entity or its
 * configuration.
 * @author T. Kostic
 * @version 1.0
 * @created 03-Jan-2024 12:08:18 PM
 */
public class ConfigurationEvent extends ActivityRecord {

	/**
	 * Date and time this event has or will become effective.
	 */
	public DateTime effectiveDateTime;
	/**
	 * Source/initiator of modification.
	 */
	public String modifiedBy;
	/**
	 * Free text remarks.
	 */
	public String remark;
	public FaultCauseType FaultCauseType;

	public ConfigurationEvent(){

	}
}//end ConfigurationEvent