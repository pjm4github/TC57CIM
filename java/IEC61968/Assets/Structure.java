package IEC61968.Assets;

import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Length;
import IEC61968.InfIEC61968.InfAssets.StructureMaterialKind;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Boolean;

/**
 * Construction holding assets such as conductors, transformers, switchgear, etc.
 * Where applicable, number of conductors can be derived from the number of
 * associated wire spacing instances.
 * @created 03-Jan-2024 12:06:39 PM
 */
public class Structure extends AssetContainer {

	/**
	 * Date fumigant was last applied.
	 */
	public Date fumigantAppliedDate;
	/**
	 * Name of fumigant.
	 */
	public String fumigantName;
	/**
	 * Visible height of structure above ground level for overhead construction (e.g.,
	 * Pole or Tower) or below ground level for an underground vault, manhole, etc.
	 * Refer to associated DimensionPropertiesInfo for other types of dimensions.
	 */
	public Length height;
	/**
	 * Material this structure is made of.
	 */
	public StructureMaterialKind materialKind;
	/**
	 * Maximum rated voltage of the equipment that can be mounted on/contained within
	 * the structure.
	 */
	public Voltage ratedVoltage;
	/**
	 * True if weeds are to be removed around asset.
	 */
	public Boolean removeWeed;
	/**
	 * Date weed were last removed.
	 */
	public Date weedRemovedDate;
	public StructureSupport StructureSupports;

	public Structure(){

	}
}//end Structure