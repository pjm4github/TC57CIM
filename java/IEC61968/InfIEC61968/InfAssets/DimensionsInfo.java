package IEC61968.InfIEC61968.InfAssets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * As applicable, the basic linear, area, or volume dimensions of an asset, asset
 * type (AssetModel) or other type of object (such as land area). Units and
 * multipliers are specified per dimension.
 * @created 03-Jan-2024 12:26:22 PM
 */
public class DimensionsInfo extends IdentifiedObject {

	/**
	 * A description of the orientation of the object relative to the dimensions. As
	 * an example, a vault may have north-south orientation for the sizeLength
	 * measurement and sizeDepth may be the height of the vault.
	 */
	public String orientation;
	/**
	 * Depth measurement.
	 */
	public Length sizeDepth;
	/**
	 * Diameter measurement.
	 */
	public Length sizeDiameter;
	/**
	 * Length measurement.
	 */
	public Length sizeLength;
	/**
	 * Width measurement.
	 */
	public Length sizeWidth;
	public Specification Specifications;

	public DimensionsInfo(){

	}
}//end DimensionsInfo