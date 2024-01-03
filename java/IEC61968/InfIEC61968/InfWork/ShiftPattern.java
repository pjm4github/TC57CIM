package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Integer;
import IEC61968.Common.Status;
import IEC61970.Base.Domain.DateTimeInterval;

/**
 * The patterns of shifts worked by people or crews.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class ShiftPattern extends WorkIdentifiedObject {

	/**
	 * Type of assignement intended to be worked on this shift, for example, temporary,
	 * standard, etc.
	 */
	public String assignmentType;
	/**
	 * Number of cycles for a temporary shift.
	 */
	public Integer cycleCount;
	public Status status;
	/**
	 * Date and time interval for which this shift pattern is valid (when it became
	 * effective and when it expires).
	 */
	public DateTimeInterval validityInterval;

	public ShiftPattern(){

	}
}//end ShiftPattern