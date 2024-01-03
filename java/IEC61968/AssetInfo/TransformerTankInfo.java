package IEC61968.AssetInfo;

import IEC61968.Assets.AssetInfo;

/**
 * Set of transformer tank data, from an equipment library.
 * @created 29-Dec-2023 5:39:35 PM
 */
public class TransformerTankInfo extends AssetInfo {

	/**
	 * Data for all the ends described by this transformer tank data.
	 */
	public TransformerEndInfo TransformerEndInfos;
	/**
	 * Power transformer data that this tank description is part of.
	 */
	public PowerTransformerInfo PowerTransformerInfo;

	public TransformerTankInfo(){

	}
}//end TransformerTankInfo