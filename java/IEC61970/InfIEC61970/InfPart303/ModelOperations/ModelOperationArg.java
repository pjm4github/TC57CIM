package IEC61970.InfIEC61970.InfPart303.ModelOperations;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Describes the role a dataset plays in a model operation.   The role is
 * applicable only in the context of a single operation.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class ModelOperationArg extends IdentifiedObject {

	/**
	 * The sequence number of the argument in an operation.  Argument entries are
	 * considered in numerical order where the operation requires an ordering.
	 * 
	 */
	public Integer sequenceNumber;
	/**
	 * The opeation for the operation argument.
	 */
	public ModelOperation ModelOperation;

	public ModelOperationArg(){

	}
}//end ModelOperationArg