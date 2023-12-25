package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Integer;

/**
 * Impedance and admittance parameters per unit length for n-wire unbalanced lines,
 * in matrix form.
 * @author Tom
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
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

	public void finalize() throws Throwable {
		super.finalize();
	}

}