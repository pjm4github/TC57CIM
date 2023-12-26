package IEC61970.Base.Wires;

import IEC61970.Base.Domain.Susceptance;
import IEC61970.Base.Domain.Conductance;
import IEC61970.Base.Domain.Integer;

/**
 * A non linear shunt compensator bank or section admittance value.
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class NonlinearShuntCompensatorPoint {

	/**
	 * Positive sequence shunt (charging) susceptance per section
	 */
	public Susceptance b;
	/**
	 * Zero sequence shunt (charging) susceptance per section
	 */
	public Susceptance b0;
	/**
	 * Positive sequence shunt (charging) conductance per section
	 */
	public Conductance g;
	/**
	 * Zero sequence shunt (charging) conductance per section
	 */
	public Conductance g0;
	/**
	 * The number of the section.
	 */
	public Integer sectionNumber;

	public NonlinearShuntCompensatorPoint(){

	}
}//end NonlinearShuntCompensatorPoint