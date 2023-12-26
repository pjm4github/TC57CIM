package IEC61970.Base.Wires;


/**
 * Common type for per-length impedance electrical catalogues.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PerLengthImpedance extends PerLengthLineParameter {

	/**
	 * All line segments described by this per-length impedance.
	 */
	public ACLineSegment ACLineSegments;

	public PerLengthImpedance(){

	}
}//end PerLengthImpedance