package IEC61970.InfIEC61970.InfPart303.ModelOperations;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An operation performed on models.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class ModelOperation extends IdentifiedObject {

	/**
	 * Sequence number within a operation sequence, lower is first.   Normally starts
	 * with 1.
	 */
	public Integer sequenceNumber;
	/**
	 * The type of the model operation.
	 */
	public ModelOperationDescription ModelOperationDescription;

	public ModelOperation(){

	}
}//end ModelOperation