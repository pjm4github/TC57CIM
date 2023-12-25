package TC57CIM.IEC61970.Base.Wires;


/**
 * Common type for per-length impedance electrical catalogues.
 * @author T. Kostic
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class PerLengthImpedance extends PerLengthLineParameter {

	/**
	 * All line segments described by this per-length impedance.
	 */
	public ACLineSegment ACLineSegments;

	public PerLengthImpedance(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}