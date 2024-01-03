package IEC61968.Common;

import IEC61970.Base.Domain.DateTime;
import IEC61970.Base.Domain.String;

/**
 * Current status information relevant to an entity.
 * @created 03-Jan-2024 12:13:13 PM
 */
public class Status {

	/**
	 * Date and time for which status 'value' applies.
	 */
	public DateTime dateTime;
	/**
	 * Reason code or explanation for why an object went to the current status 'value'.
	 */
	public String reason;
	/**
	 * Pertinent information regarding the current 'value', as free form text.
	 */
	public String remark;
	/**
	 * Status value at 'dateTime'; prior status changes may have been kept in
	 * instances of activity records associated with the object to which this status
	 * applies.
	 */
	public String value;

	public Status(){

	}
}//end Status