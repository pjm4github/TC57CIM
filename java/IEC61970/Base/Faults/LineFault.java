package IEC61970.Base.Faults;

import IEC61970.Base.Domain.Length;
import IEC61970.Base.Wires.ACLineSegment;

/**
 * A fault that occurs on an AC line segment at some point along the length.
 * @author kdemaree
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class LineFault extends Fault {

	/**
	 * The length to the place where the fault is located starting from terminal with
	 * sequence number 1 of the faulted line segment.
	 */
	public Length lengthFromTerminal1;
	/**
	 * The line segment of this line fault.
	 */
	public ACLineSegment ACLineSegment;

	public LineFault(){

	}
}//end LineFault