package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Susceptance;
import TC57CIM.IEC61970.Base.Domain.Conductance;
import TC57CIM.IEC61970.Base.Domain.Integer;

/**
 * A per phase non linear shunt compensator bank or section admittance value.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
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

	public void finalize() throws Throwable {

	}

}