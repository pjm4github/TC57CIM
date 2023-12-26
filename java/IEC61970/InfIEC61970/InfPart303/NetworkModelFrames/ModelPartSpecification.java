package IEC61970.InfIEC61970.InfPart303.NetworkModelFrames;

import IEC61970.Base.Core.IdentifiedObject;

/**
 * The type of model.  For example,  state estimator, planning, planning dynamics,
 * short circuit, or real-time dynamics etc.     The model must conform to a
 * profile.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class ModelPartSpecification extends IdentifiedObject {

	/**
	 * Model frame of the model part.
	 */
	public ModelAuthoritySet FrameworkPart;

	public ModelPartSpecification(){

	}
}//end ModelPartSpecification