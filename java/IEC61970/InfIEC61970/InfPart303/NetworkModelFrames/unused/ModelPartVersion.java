package IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.unused;

import IEC61970.InfIEC61970.InfPart303.NetworkModelFrames.ModelPartVersion;
import IEC61970.Part303.GenericDataset.InstanceSet;

/**
 * Versioned instance of a model part.
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class ModelPartVersion {

	/**
	 * Model part of the model part version.
	 */
	public ModelPartVersion ModelPart;
	/**
	 * Dataset of the model part version.
	 */
	public InstanceSet FullModelDataset;

	public ModelPartVersion(){

	}
}//end ModelPartVersion