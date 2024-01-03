package IEC61968.Assets;

import IEC61970.Base.Domain.Integer;

/**
 * A duct contains individual wires in the layout as specified with associated
 * wire spacing instances; number of them gives the number of conductors in this
 * duct.
 * @created 03-Jan-2024 12:04:02 PM
 */
public class DuctBank extends AssetContainer {

	/**
	 * Number of circuits in duct bank. Refer to associations between a duct
	 * (ConductorAsset) and an ACLineSegment to understand which circuits are in which
	 * ducts.
	 */
	public Integer circuitCount;

	public DuctBank(){

	}
}//end DuctBank