package IEC61968.InfIEC61968.InfAssets;

import IEC61968.Assets.Structure;

/**
 * Tower asset. Dimensions of the Tower are specified in associated DimensionsInfo
 * class.
 * When used for planning purposes, a transmission tower carrying two 3-phase
 * circuits will have 2 instances of Connection, each of which will have 3
 * MountingPoint instances, one for each phase all with coordinates relative to a
 * common origin on the tower. (It may also have a 3rd Connection with a single
 * MountingPoint for the Neutral line).
 * @created 03-Jan-2024 12:27:38 PM
 */
public class Tower extends Structure {

	/**
	 * Construction structure on the tower.
	 */
	public TowerConstructionKind constructionKind;

	public Tower(){

	}
}//end Tower