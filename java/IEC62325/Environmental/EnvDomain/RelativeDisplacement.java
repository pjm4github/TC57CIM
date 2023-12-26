package IEC62325.Environmental.EnvDomain;

import IEC61970.Base.Domain.Displacement;

/**
 * Vertical displacement relative to either sealevel, ground or the center of the
 * earth.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:38 PM
 */
public class RelativeDisplacement {

	public Displacement displacement;
	public RelativeDisplacementKind kind;

	public RelativeDisplacement(){

	}
}//end RelativeDisplacement