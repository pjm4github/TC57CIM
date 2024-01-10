package IEC61968.Assets;

import IEC61968.InfIEC61968.InfAssets.AnchorKind;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Length;
import IEC61970.Base.Domain.AngleDegrees;
import IEC61968.InfIEC61968.InfAssets.StructureSupportKind;
import IEC61970.Base.Domain.String;

/**
 * Support for structure assets.
 * @created 07-Jan-2024 9:49:01 PM
 */
public class StructureSupport extends Asset {

	/**
	 * (if anchor) Kind of anchor.
	 */
	public AnchorKind anchorKind;
	/**
	 * (if anchor) Number of rods used.
	 */
	public Integer anchorRodCount;
	/**
	 * (if anchor) Length of rod used.
	 */
	public Length anchorRodLength;
	/**
	 * Direction of this support structure.
	 */
	public AngleDegrees direction;
	/**
	 * Kind of structure support.
	 */
	public StructureSupportKind kind;
	/**
	 * Length of this support structure.
	 */
	public Length length;
	/**
	 * Size of this support structure.
	 */
	public String size;

	public StructureSupport(){

	}
}//end StructureSupport