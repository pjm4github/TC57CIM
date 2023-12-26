package IEC61968.Assets;

import IEC61968.Common.Document;

/**
 * A grouping of assets created for a purpose such as fleet analytics, inventory
 * or compliance management.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class AssetGroup extends Document {

	/**
	 * Kind of asset group this asset group is.
	 */
	public AssetGroupKind kind;
	public AnalyticScore AnalyticScore;
	public Asset Asset;

	public AssetGroup(){

	}
}//end AssetGroup