package IEC61970.InfIEC61970.InfPart303.ModelOperations;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * The type of custom operation dataset role for an operation description.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class ModelOperationArgDescription extends IdentifiedObject {

	/**
	 * 
	 * The maximum multiplicity of the instance arguments that should be supplied for
	 * a single operation.     Use -1 to indicate unlimited. 
	 */
	public Integer multiplicityMaximum;
	/**
	 * 
	 * The minimum multiplicity of the instance arguments that should be supplied for
	 * a single operation.     Use zero to indicate optional. 
	 */
	public Integer multiplicityMinimum;
	/**
	 * The type of operation for this type of dataset role.   Operations referencing
	 * the dataset role type should only belong to operations that reference the
	 * operation type.
	 */
	public ModelOperationDescription ModelOperationDefinition;

	public ModelOperationArgDescription(){

	}
}//end ModelOperationArgDescription