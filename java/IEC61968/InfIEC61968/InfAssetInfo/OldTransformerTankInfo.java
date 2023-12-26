package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.Voltage;
import IEC61968.AssetInfo.TransformerTankInfo;

/**
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OldTransformerTankInfo extends TransformerTankInfo {

	/**
	 * Kind of construction for this transformer.
	 */
	public TransformerConstructionKind constructionKind;
	/**
	 * Weight of core and coils in transformer.
	 */
	public Mass coreCoilsWeight;
	/**
	 * Core kind of this transformer product.
	 */
	public TransformerCoreKind coreKind;
	/**
	 * Function of this transformer.
	 */
	public TransformerFunctionKind function;
	/**
	 * Basic insulation level of neutral.
	 */
	public Voltage neutralBIL;
	/**
	 * Kind of oil preservation system.
	 */
	public OilPreservationKind oilPreservationKind;

	public OldTransformerTankInfo(){

	}
}//end OldTransformerTankInfo