package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.AngleDegrees;
import TC57CIM.IEC61970.Base.Domain.Reactance;

/**
 * Describes a tap changer with a linear relation between the tap step and the
 * phase angle difference across the transformer. This is a mathematical model
 * that is an approximation of a real phase tap changer.
 * The phase angle is computed as stepPhaseShitfIncrement times the tap position.
 * The secondary side voltage magnitude is the same as at the primary side.
 * @author SELAOST1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class PhaseTapChangerLinear extends PhaseTapChanger {

	/**
	 * Phase shift per step position. A positive value indicates a positive phase
	 * shift from the winding where the tap is located to the other winding (for a two-
	 * winding transformer).
	 * The actual phase shift increment might be more accurately computed from the
	 * symmetrical or asymmetrical models or a tap step table lookup if those are
	 * available.
	 */
	public AngleDegrees stepPhaseShiftIncrement;
	/**
	 * The reactance depend on the tap position according to a "u" shaped curve. The
	 * maximum reactance (xMax) appear at the low and high tap positions.
	 */
	public Reactance xMax;
	/**
	 * The reactance depend on the tap position according to a "u" shaped curve. The
	 * minimum reactance (xMin) appear at the mid tap position.
	 */
	public Reactance xMin;

	public PhaseTapChangerLinear(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}