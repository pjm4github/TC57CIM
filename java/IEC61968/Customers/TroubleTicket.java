package IEC61968.Customers;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.Boolean;
import IEC61968.Operations.Incident;
import IEC61968.Common.Document;

/**
 * @author T. Kostic
 * @version 1.0
 * @created 03-Jan-2024 12:18:31 PM
 */
public class TroubleTicket extends Document {

	/**
	 * Free-form comment associated with the trouble call for example, "customer
	 * reported a large flash", etc.
	 */
	public String comment;
	/**
	 * Date and time the trouble has been reported.
	 */
	public DateTime dateTimeOfReport;
	/**
	 * Indicates whether the first responder such as police, fire department etc.has
	 * been notified and whether they are on site or en route.
	 */
	public String firstResponderStatus;
	/**
	 * Set to true if the outage report indicated that other neighbors are also out of
	 * power.
	 */
	public Boolean multiplePremises;
	/**
	 * Indicates how the customer reported trouble.
	 */
	public TroubleReportingKind reportingKind;
	/**
	 * Date and time this trouble ticket has been resolved.
	 */
	public DateTime resolvedDateTime;
	/**
	 * Trouble code (e.g., power down, flickering lights, partial power, etc).
	 */
	public String troubleCode;
	/**
	 * All hazards reported with this trouble ticket.
	 */
	public IncidentHazard IncidentHazard;
	/**
	 * Customer for whom this trouble ticket is relevant.
	 */
	public Customer Customer;
	/**
	 * Incident reported in this trouble ticket
	 */
	public Incident Incident;

	public TroubleTicket(){

	}
}//end TroubleTicket