package IEC61970.Base.Protection;

import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A reclose sequence (open and close) is defined for each possible reclosure of a
 * breaker.
 * @created 25-Dec-2023 8:32:03 PM
 */
public class RecloseSequence extends IdentifiedObject {

	/**
	 * Indicates the time lapse before the reclose step will execute a reclose.
	 */
	public Seconds recloseDelay;
	/**
	 * Indicates the ordinal position of the reclose step relative to other steps in
	 * the sequence.
	 */
	public Integer recloseStep;

	public RecloseSequence(){

	}
}//end RecloseSequence