package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Core.IdentifiedObject;

/**
 * Describes a tabular curve for how the phase angle difference and impedance
 * varies with the tap step.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class PhaseTapChangerTable extends IdentifiedObject {

	/**
	 * The phase tap changers to which this phase tap table applies.
	 */
	public PhaseTapChangerTabular PhaseTapChangerTabular;

	public PhaseTapChangerTable(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}