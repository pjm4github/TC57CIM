package IEC61970.InfIEC61970.InfPart303.NetworkModelProjects;

import IEC61970.Base.Domain.Date;

/**
 * Represent the base lifecycle of a functional model change that could be a
 * construction of new elements.
 * @author sveinols
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class PowerSystemProjectLifecycle_TO_BE_DELETED {

	/**
	 * The date the Power System Project is in cancelled stage.
	 */
	public Date cancelled;
	/**
	 * The date Power System Project is in committed stage.
	 */
	public Date committed;
	/**
	 * The date Power System Project is in build stage.
	 */
	public Date inBuild;
	/**
	 * The date Power System Project is in planning stage.
	 */
	public Date inPlan;

	public PowerSystemProjectLifecycle_TO_BE_DELETED(){

	}
}//end PowerSystemProjectLifecycle_TO_BE_DELETED