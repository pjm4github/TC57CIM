package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Susceptance;
import IEC61970.Base.Domain.Conductance;
import IEC61970.Base.Domain.Integer;

/**
 * A per phase non linear shunt compensator bank or section admittance value.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class NonlinearShuntCompensatorPhasePoint {

	/**
	 * Positive sequence shunt (charging) susceptance per section
	 */
	public Susceptance b;
	/**
	 * Positive sequence shunt (charging) conductance per section
	 */
	public Conductance g;
	/**
	 * The number of the section.
	 */
	public Integer sectionNumber;

	public NonlinearShuntCompensatorPhasePoint(){

	}
}//end NonlinearShuntCompensatorPhasePoint