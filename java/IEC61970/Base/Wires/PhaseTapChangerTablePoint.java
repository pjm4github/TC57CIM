package IEC61970.Base.Wires;

import IEC61970.Base.Domain.AngleDegrees;

/**
 * Describes each tap step in the phase tap changer tabular curve.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PhaseTapChangerTablePoint extends TapChangerTablePoint {

	/**
	 * The angle difference in degrees. A positive value indicates a positive phase
	 * shift from the winding where the tap is located to the other winding (for a two-
	 * winding transformer).
	 */
	public AngleDegrees angle;
	/**
	 * The table of this point.
	 */
	public PhaseTapChangerTable PhaseTapChangerTable;

	public PhaseTapChangerTablePoint(){

	}
}//end PhaseTapChangerTablePoint