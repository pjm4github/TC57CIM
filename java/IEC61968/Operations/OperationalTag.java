package IEC61968.Operations;

import IEC61970.Base.Core.PowerSystemResource;
import IEC61968.Assets.Asset;
import IEC61968.Common.Document;

/**
 * Operational tag placed on a power system resource or asset in the context of
 * switching plan execution or other work in the field.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OperationalTag extends Document {

	/**
	 * Power system resource on which this tag has been placed.
	 */
	public PowerSystemResource PowerSystemResource;
	/**
	 * Asset on which this tag has been placed.
	 */
	public Asset Asset;

	public OperationalTag(){

	}
}//end OperationalTag