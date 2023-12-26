package IEC61968.Common;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.DateTimeInterval;
import IEC61968.Work.Work;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Meeting time and location.
 * @created 25-Dec-2023 8:45:18 PM
 */
public class Appointment extends IdentifiedObject {

	/**
	 * True if requested to call customer when someone is about to arrive at their
	 * premises.
	 */
	public Boolean callAhead;
	/**
	 * Date and time reserved for appointment.
	 */
	public DateTimeInterval meetingInterval;
	/**
	 * All works for this appointment.
	 */
	public Work Works;

	public Appointment(){

	}
}//end Appointment