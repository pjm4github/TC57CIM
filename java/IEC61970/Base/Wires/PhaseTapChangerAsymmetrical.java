package IEC61970.Base.Wires;

import IEC61970.Base.Domain.AngleDegrees;

/**
 * Describes the tap model for an asymmetrical phase shifting transformer in which
 * the difference voltage vector adds to the primary side voltage. The angle
 * between the primary side voltage and the difference voltage is named the
 * winding connection angle. The phase shift depends on both the difference
 * voltage magnitude and the winding connection angle.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PhaseTapChangerAsymmetrical extends PhaseTapChangerNonLinear {

	/**
	 * The phase angle between the in-phase winding and the out-of -phase winding used
	 * for creating phase shift. The out-of-phase winding produces what is known as
	 * the difference voltage.  Setting this angle to 90 degrees is not the same as a
	 * symmetrical transformer.
	 */
	public AngleDegrees windingConnectionAngle;

	public PhaseTapChangerAsymmetrical(){

	}
}//end PhaseTapChangerAsymmetrical