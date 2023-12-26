package IEC61970.Base.Wires;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * Describes a tabular curve for how the phase angle difference and impedance
 * varies with the tap step.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PhaseTapChangerTable extends IdentifiedObject {

	/**
	 * The phase tap changers to which this phase tap table applies.
	 */
	public PhaseTapChangerTabular PhaseTapChangerTabular;

	public PhaseTapChangerTable(){

	}
}//end PhaseTapChangerTable