package IEC61970.InfIEC61970.InfPart303.NetworkModelFrames;

import IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.unused.ModelFrameType;

/**
 * The type of alternate model frame.  For example, it could be generator group
 * used to represent generators in state estimator, planning, planning dynamics,
 * short circuit, or real-time dynamics etc., but does not specifically represent
 * any one alternative model. This need to know what objects to be removed in the
 * realization of any one alternate model.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:58 PM
 */
public class FrameworkPart extends ModelAuthoritySet {

	/**
	 * Model frame type of the model frame.
	 */
	public ModelFrameType ModelFrameType;

	public FrameworkPart(){

	}
}//end FrameworkPart