package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.String;
import IEC61968.Assets.Procedure;
import IEC61968.Assets.CatalogAssetType;

/**
 * A pre-planned job model containing labor, material, and accounting requirements
 * for standardized job planning.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CompatibleUnit extends WorkDocument {

	/**
	 * Estimated total cost for perfoming CU.
	 */
	public Money estCost;
	/**
	 * The quantity, unit of measure, and multiplier at the CU level that applies to
	 * the materials.
	 */
	public String quantity;
	public DesignLocationCU DesignLocationCUs;
	public CUGroup CUGroup;
	public Procedure Procedures;
	public CatalogAssetType GenericAssetModel;

	public CompatibleUnit(){

	}
}//end CompatibleUnit