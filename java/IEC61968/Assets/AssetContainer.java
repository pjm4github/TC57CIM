package IEC61968.Assets;


/**
 * Asset that is aggregation of other assets such as conductors, transformers,
 * switchgear, land, fences, buildings, equipment, vehicles, etc.
 * @created 03-Jan-2024 12:00:19 PM
 */
public class AssetContainer extends Asset {

	/**
	 * All seals applied to this asset container.
	 */
	public Seal Seals;

	public AssetContainer(){

	}
}//end AssetContainer