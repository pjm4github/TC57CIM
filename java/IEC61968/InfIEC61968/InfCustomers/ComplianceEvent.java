package IEC61968.InfIEC61968.InfCustomers;

import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.ActivityRecord;

/**
 * Compliance events are used for reporting regulatory or contract compliance
 * issues and/or variances. These might be created as a consequence of local
 * business processes and associated rules. It is anticipated that this class will
 * be customised extensively to meet local implementation needs.
 * Use inherited 'type' to indicate that, for example, expected performance will
 * not be met or reported as mandated.
 * @created 29-Dec-2023 9:25:00 PM
 */
public class ComplianceEvent extends ActivityRecord {

	/**
	 * The deadline for compliance.
	 */
	public DateTime deadline;

	public ComplianceEvent(){

	}
}//end ComplianceEvent