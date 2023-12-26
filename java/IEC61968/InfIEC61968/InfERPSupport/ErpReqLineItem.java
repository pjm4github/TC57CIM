import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.Money;
import IEC61970.Base.Domain.Date;
import IEC61970.Base.Domain.Integer;
import IEC61968.Common.Status;

/**
 * Information that describes a requested item and its attributes.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpReqLineItem extends ErpIdentifiedObject {

	public String code;
	/**
	 * Cost of material.
	 */
	public Money cost;
	public Date deliveryDate;
	/**
	 * Quantity of item requisitioned.
	 */
	public Integer quantity;
	public Status status;
	public ErpPOLineItem ErpPOLineItem;
	public ErpRequisition ErpRequisition;

	public ErpReqLineItem(){

	}
}//end ErpReqLineItem