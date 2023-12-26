package IEC61968.Assets;

import IEC61970.Base.Domain.String;

/**
 * Documents the result of one inspection, for a given attribute of an asset.
 * @created 25-Dec-2023 8:45:22 PM
 */
public class InspectionDataSet extends ProcedureDataSet {

	/**
	 * Description of the conditions of the location where the asset resides.
	 */
	public String locationCondition;

	public InspectionDataSet(){

	}
}//end InspectionDataSet