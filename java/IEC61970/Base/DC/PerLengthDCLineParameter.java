package IEC61970.Base.DC;

import IEC61970.Base.Domain.CapacitancePerLength;
import IEC61970.Base.Domain.InductancePerLength;
import IEC61970.Base.Domain.ResistancePerLength;
import IEC61970.Base.Wires.PerLengthLineParameter;

/**
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PerLengthDCLineParameter extends PerLengthLineParameter {

	/**
	 * Capacitance per unit of length of the DC line segment; significant for cables
	 * only.
	 */
	public CapacitancePerLength capacitance;
	/**
	 * Inductance per unit of length of the DC line segment.
	 */
	public InductancePerLength inductance;
	/**
	 * Resistance per length of the DC line segment.
	 */
	public ResistancePerLength resistance;
	/**
	 * All line segments described by this set of per-length parameters.
	 */
	public DCLineSegment DCLineSegments;

	public PerLengthDCLineParameter(){

	}
}//end PerLengthDCLineParameter