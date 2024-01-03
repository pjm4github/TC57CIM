package IEC61968.InfIEC61968.InfAssets;

import IEC61968.Assets.Medium;
import IEC61968.Common.Document;

/**
 * Specification can be used for various purposes relative to an asset, a logical
 * device (PowerSystemResource), location, etc. Examples include documents
 * supplied by manufacturers such as asset installation instructions, asset
 * maintenance instructions, etc.
 * @created 03-Jan-2024 12:27:23 PM
 */
public class Specification extends Document {

	public AssetPropertyCurve AssetPropertyCurves;
	public Medium Mediums;

	public Specification(){

	}
}//end Specification