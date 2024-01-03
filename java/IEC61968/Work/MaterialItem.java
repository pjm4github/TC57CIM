package IEC61968.Work;

import IEC61970.Base.Domain.IntegerQuantity;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The physical consumable supply used for work and other purposes. It includes
 * items such as nuts, bolts, brackets, glue, etc.
 * @created 02-Jan-2024 10:04:43 PM
 */
public class MaterialItem extends IdentifiedObject {

	/**
	 * Quantity of material used.
	 */
	public IntegerQuantity quantity;

	public MaterialItem(){

	}
}//end MaterialItem