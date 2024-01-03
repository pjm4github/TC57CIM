package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Displacement;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Identification, spacing and configuration of the wires of a conductor with
 * respect to a structure.
 * @created 03-Jan-2024 11:56:56 AM
 */
public class WirePosition extends IdentifiedObject {

	/**
	 * Signed horizontal distance from the wire at this position to a common reference
	 * point.
	 */
	public Displacement xCoord;
	/**
	 * Signed vertical distance from the wire at this position: above ground (positive
	 * value) or burial depth below ground (negative value).
	 */
	public Displacement yCoord;
	public WirePhaseInfo WirePhaseInfo;

	public WirePosition(){

	}
}//end WirePosition