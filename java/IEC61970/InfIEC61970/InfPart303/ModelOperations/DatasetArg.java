package IEC61970.InfIEC61970.InfPart303.ModelOperations;

import IEC61970.Part303.GenericDataset.InstanceSet;

/**
 * A model operation argument referencing a dataset instance.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class DatasetArg extends ModelOperationArg {

	/**
	 * The type of role for this dataset role.   Should only reference role types that
	 * belong to the operation type of the associated operation.
	 */
	public DatasetArgDescription OperationDatasetArgDescription;
	/**
	 * Dataset referenced by this argument of a model operation..
	 */
	public InstanceSet Dataset;

	public DatasetArg(){

	}
}//end DatasetArg