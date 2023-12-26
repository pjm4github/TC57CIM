package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Susceptance;
import IEC61970.Base.Domain.Conductance;

/**
 * A per phase linear shunt compensator has banks or sections with equal
 * admittance values.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
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
}//end LinearShuntCompensatorPhase