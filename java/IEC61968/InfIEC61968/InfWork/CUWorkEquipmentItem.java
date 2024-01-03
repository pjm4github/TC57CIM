package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.CostRate;
import IEC61968.Common.Status;
import IEC61968.Work.WorkAsset;

/**
 * Compatible unit for various types of WorkEquipmentAssets, including vehicles.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CUWorkEquipmentItem extends WorkIdentifiedObject {

	/**
	 * The equipment type code.
	 */
	public String equipCode;
	/**
	 * Standard usage rate for the type of vehicle.
	 */
	public CostRate rate;
	public Status status;
	public CompatibleUnit CompatibleUnits;
	public WorkAsset TypeAsset;

	public CUWorkEquipmentItem(){

	}
}//end CUWorkEquipmentItem