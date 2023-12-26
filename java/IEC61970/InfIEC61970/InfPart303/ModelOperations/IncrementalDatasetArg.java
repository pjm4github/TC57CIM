package IEC61970.InfIEC61970.InfPart303.ModelOperations;

import IEC61970.Part303.GenericDataset.ChangeSet;

/**
 * A generic model operation argument referencing an incremental change
 * description.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public class IncrementalDatasetArg extends ModelOperationArg {

	public IncrementalDatasetArgDescription IncrementalDatasetArgDescription;
	public ChangeSet IncrementalDataset;

	public IncrementalDatasetArg(){

	}
}//end IncrementalDatasetArg