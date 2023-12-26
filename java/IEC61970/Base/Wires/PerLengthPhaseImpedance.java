package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Integer;

/**
 * Impedance and admittance parameters per unit length for n-wire unbalanced lines,
 * in matrix form.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PerLengthPhaseImpedance extends PerLengthImpedance {

	/**
	 * Number of phase, neutral, and other wires retained. Constrains the number of
	 * matrix elements and the phase codes that can be used with this matrix.
	 */
	public Integer conductorCount;
	/**
	 * All data that belong to this conductor phase impedance.
	 */
	public PhaseImpedanceData PhaseImpedanceData;

	public PerLengthPhaseImpedance(){

	}
}//end PerLengthPhaseImpedance