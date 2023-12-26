package IEC61968.Operations;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Customers.TroubleTicket;

/**
 * Document describing the consequence of an unplanned outage in a part of the
 * electrical network. For the purposes of this model, an unplanned outage refers
 * to a state where energy is not delivered; such as, customers out of service, a
 * street light is not served, etc.
 * A unplanned outage may be created upon:
 * - impacts the SAIDI calculation
 * - a breaker trip,
 * - a fault indicator status change,
 * - a meter event indicating customer outage,
 * - a reception of one or more customer trouble calls, or
 * - an operator command, reflecting information obtained from the field crew.
 * Outage restoration may be performed using a switching plan which complements
 * the outage information with detailed switching activities, including the
 * relationship to the crew and work.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class UnplannedOutage extends Outage {

	/**
	 * The cause of this outage.  This is the cause that is used to present to
	 * external entities.  That is, the cause is weather, equipment failure, etc.
	 * 
	 * Note: At present, this is a free text; could be replaced with a separate
	 * associated class in case we have multiple causes (e.g. OutageCauseType,
	 * inheriting from IdentifiedObject).
	 */
	public String cause;
	public OutageCauseKind causeKind;
	/**
	 * The earliest start time of the Outage - as reported by some system or individual
	 */
	public DateTime reportedStartTime;
	public TroubleTicket TroubleTicket;

	public UnplannedOutage(){

	}
}//end UnplannedOutage