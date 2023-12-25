package TC57CIM.IEC61970.Base.Faults;

import TC57CIM.IEC61970.Base.Domain.Length;
import TC57CIM.IEC61970.Base.Wires.ACLineSegment;

/**
 * A fault that occurs on an AC line segment at some point along the length.
 * @author kdemaree
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}