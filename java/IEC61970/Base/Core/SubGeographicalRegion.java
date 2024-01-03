package IEC61970.Base.Core;

import IEC61970.Base.Wires.Line;

/**
 * A subset of a geographical region of a power system network model.
 * @created 02-Jan-2024 10:37:43 PM
 */
public class SubGeographicalRegion extends IdentifiedObject {

	/**
	 * The lines within the sub-geographical region.
	 */
	public Line Lines;
	/**
	 * The substations in this sub-geographical region.
	 */
	public Substation Substations;

	public SubGeographicalRegion(){

	}
}//end SubGeographicalRegion