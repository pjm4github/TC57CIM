package TC57CIM.IEC61970.Base.Wires;

import TC57CIM.IEC61970.Base.Domain.Susceptance;
import TC57CIM.IEC61970.Base.Domain.Conductance;

/**
 * A linear shunt compensator has banks or sections with equal admittance values.
 * @author selaost1
 * @version 1.0
 * @created 15-Dec-2023 4:38:28 PM
 */
public class LinearShuntCompensator extends ShuntCompensator {

	/**
	 * Zero sequence shunt (charging) susceptance per section
	 */
	public Susceptance b0PerSection;
	/**
	 * Positive sequence shunt (charging) susceptance per section
	 */
	public Susceptance bPerSection;
	/**
	 * Zero sequence shunt (charging) conductance per section
	 */
	public Conductance g0PerSection;
	/**
	 * Positive sequence shunt (charging) conductance per section
	 */
	public Conductance gPerSection;

	public LinearShuntCompensator(){

	}

	public void finalize() throws Throwable {
		super.finalize();
	}

}