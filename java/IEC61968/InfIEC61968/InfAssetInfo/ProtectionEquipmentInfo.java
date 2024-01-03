package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.CurrentFlow;
import IEC61968.Assets.AssetInfo;

/**
 * Properties of protection equipment asset.
 * @created 29-Dec-2023 6:23:04 PM
 */
public class ProtectionEquipmentInfo extends AssetInfo {

	/**
	 * Actual ground trip for this type of relay, if applicable.
	 */
	public CurrentFlow groundTrip;
	/**
	 * Actual phase trip for this type of relay, if applicable.
	 */
	public CurrentFlow phaseTrip;

	public ProtectionEquipmentInfo(){

	}
}//end ProtectionEquipmentInfo