package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Integer;
import TC57CIM.IEC61970.Base.Core.PowerSystemResource;

/**
 * Represents a single wire of an alternating current line segment.
 * @author kdemaree
 * @version 1.0
 * @created 15-Dec-2023 4:38:26 PM
 */
public class ACLineSegmentPhase extends PowerSystemResource {

	/**
	 * The phase connection of the wire at both ends.
	 */
	public SinglePhaseKind phase;
	/**
	 * Number designation for this line segment phase. Each line segment phase within
	 * a line segment should have a unique sequence number. This is useful for
	 * unbalanced modeling to bind the mathematical model (PhaseImpedanceData of
	 * PerLengthPhaseImpedance) with the connectivity model (this class) and the
	 * physical model (WirePosition) without tight coupling.
	 */
	public Integer sequenceNumber;
	/**
	 * The line segment to which the phase belongs.
	 */
	public ACLineSegment ACLineSegment;

	public ACLineSegmentPhase(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}