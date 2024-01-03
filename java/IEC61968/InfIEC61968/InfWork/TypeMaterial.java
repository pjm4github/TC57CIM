package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Boolean;
import IEC61968.Work.MaterialItem;

/**
 * Documentation for a generic material item that may be used for design, work and
 * other purposes. Any number of MaterialItems manufactured by various vendors may
 * be used to perform this TypeMaterial.
 * Note that class analagous to "AssetModel" is not used for material items. This
 * is because in some cases, for example, a utility sets up a Master material
 * record for a 3 inch long half inch diameter steel bolt and they do not
 * necessarily care what specific supplier is providing the material item. As
 * different vendors are used to supply the part, the Stock Code of the material
 * item can stay the same. In other cases, each time the vendor changes, a new
 * stock code is set up so they can track material used by vendor. Therefore a
 * Material Item "Model" is not typically needed.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class TypeMaterial extends WorkDocument {

	/**
	 * The type of cost to which this Material Item belongs.
	 */
	public String costType;
	/**
	 * The estimated unit cost of this type of material, either for a unit cost or
	 * cost per unit length. Cost is for material or asset only and does not include
	 * labor to install/construct or configure it.
	 */
	public Money estUnitCost;
	/**
	 * The value, unit of measure, and multiplier for the quantity.
	 */
	public String quantity;
	/**
	 * True if item is a stock item (default).
	 */
	public Boolean stockItem;
	public ErpReqLineItem ErpReqLineItems;
	public MaterialItem MaterialItems;

	public TypeMaterial(){

	}
}//end TypeMaterial