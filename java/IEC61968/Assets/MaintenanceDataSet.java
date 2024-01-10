package IEC61968.Assets;

import IEC61970.Base.Domain.String;

/**
 * The result of a maintenance activity, a type of Procedure, for a given
 * attribute of an asset.
 * @created 07-Jan-2024 9:48:17 PM
 */
public class MaintenanceDataSet extends ProcedureDataSet {

	/**
	 * Condition of asset just following maintenance procedure.
	 */
	public String conditionAfter;
	/**
	 * Description of the condition of the asset just prior to maintenance being
	 * performed.
	 */
	public String conditionBefore;
	/**
	 * Code for the type of maintenance performed.
	 */
	public String maintCode;

	public MaintenanceDataSet(){

	}
}//end MaintenanceDataSet