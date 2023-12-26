package IEC61968.Assets;

import IEC61968.Common.Location;
import IEC61968.Common.Hazard;

/**
 * Potential hazard related to the location of an asset. Examples are trees
 * growing under overhead power lines, a park being located by a substation (i.e.,
 * children climb fence to recover a ball), a lake near an overhead distribution
 * line (fishing pole/line contacting power lines), dangerous neighbour, etc.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AssetLocationHazard extends Hazard {

	/**
	 * Kind of hazard.
	 */
	public AssetHazardKind kind;
	/**
	 * The location of this hazard.
	 */
	public Location Locations;

	public AssetLocationHazard(){

	}
}//end AssetLocationHazard