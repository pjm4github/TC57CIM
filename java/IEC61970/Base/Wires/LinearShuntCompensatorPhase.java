package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Susceptance;
import TC57CIM.IEC61970.Base.Domain.Conductance;

/**
 * A per phase linear shunt compensator has banks or sections with equal
 * admittance values.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class LinearShuntCompensatorPhase extends ShuntCompensatorPhase {

	/**
	 * Susceptance per section of the phase if shunt compensator is wye connected.
	 * Susceptance per section phase to phase if shunt compensator is delta connected.
	 */
	public Susceptance bPerSection;
	/**
	 * Conductance per section for this phase if shunt compensator is wye connected.
	 * Conductance per section phase to phase if shunt compensator is delta connected.
	 */
	public Conductance gPerSection;

	public LinearShuntCompensatorPhase(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}