import IEC61968.Common.Status;

/**
 * An individual entry on an ErpTimeSheet.
 * @created 25-Dec-2023 8:45:21 PM
 */
public class ErpTimeEntry extends ErpIdentifiedObject {

	public Status status;
	public ErpProjectAccounting ErpProjectAccounting;

	public ErpTimeEntry(){

	}
}//end ErpTimeEntry