package IEC61970.Base.StateVariables;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Wires.ShuntCompensator;

/**
 * State variable for the number of sections in service for a shunt compensator.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:32:03 PM
 */
public class SvShuntCompensatorSections extends StateVariable {

	/**
	 * The number of sections in service as a continous variable. To get integer value
	 * scale with ShuntCompensator.bPerSection.
	 */
	public Float sections;
	/**
	 * The shunt compensator for which the state applies.
	 */
	public ShuntCompensator ShuntCompensator;

	public SvShuntCompensatorSections(){

	}
}//end SvShuntCompensatorSections