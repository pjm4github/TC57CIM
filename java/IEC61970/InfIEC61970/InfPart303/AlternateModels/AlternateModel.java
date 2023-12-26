package IEC61970.InfIEC61970.InfPart303.AlternateModels;

import IEC61970.Base.Core.IdentifiedObject;
import IEC61970.Part303.GenericDataset.DataSet;

/**
 * @author 222206
 * @version 1.0
 * @created 25-Dec-2023 8:31:54 PM
 */
public class AlternateModel extends IdentifiedObject {

	/**
	 * The group of alternate models for which one alternate is used.
	 */
	public AlternateModelGroup AlternateModelGroup;
	/**
	 * The data belonging to the alternate model.
	 */
	public DataSet Dataset;

	public AlternateModel(){

	}
}//end AlternateModel