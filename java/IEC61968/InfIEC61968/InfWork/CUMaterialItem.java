package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.IntegerQuantity;
import IEC61968.Common.Status;

/**
 * Compatible unit of a consumable supply item. For example, nuts, bolts, brackets,
 * glue, etc.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class CUMaterialItem extends WorkIdentifiedObject {

	/**
	 * Code for material.
	 */
	public String corporateCode;
	/**
	 * Quantity of the TypeMaterial for this CU, used to determine estimated costs
	 * based on a per unit cost or a cost per unit length specified in the
	 * TypeMaterial.
	 */
	public IntegerQuantity quantity;
	public Status status;
	public TypeMaterial TypeMaterial;
	public CompatibleUnit CompatibleUnits;

	public CUMaterialItem(){

	}
}//end CUMaterialItem