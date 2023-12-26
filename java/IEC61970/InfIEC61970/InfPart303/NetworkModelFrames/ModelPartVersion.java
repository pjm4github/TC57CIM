package IEC61970.InfIEC61970.InfPart303.NetworkModelFrames;

import IEC61970.Part303.GenericDataset.DataSet;

/**
 * This is a version of a part of a model.  New instances of this class with new
 * identity are instantiated upon changes to the content of this class or changes
 * to the associated data set.  Instances of this class are considered immutable.
 * The case audit trail can reference this immutable data to exactly reproduce a
 * case.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class ModelPartVersion extends Model_TO_BE_DELETED {

	/**
	 * Model specification of the modelt.
	 */
	private ModelPartSpecification ModelSpecification;
	public DataSet m_DataSet;
	public CompleteModel_TO_BE_DELETED m_CompleteModel_TO_BE_DELETED;

	public ModelPartVersion(){

	}
}//end ModelPartVersion