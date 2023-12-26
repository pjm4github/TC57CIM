package IEC61968.Assets;

import IEC61970.Base.Domain.String;

/**
 * Results of testing done by a lab.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class LabTestDataSet extends ProcedureDataSet {

	/**
	 * Conclusion drawn from test results.
	 */
	public String conclusion;
	/**
	 * Description of confidence in conclusion.
	 */
	public String conclusionConfidence;
	/**
	 * Reason for performing test.
	 */
	public TestReason reasonForTest;
	/**
	 * Identity of lab equipment used to perform test.
	 */
	public String testEquipmentID;
	/**
	 * Specimen on which lab testing done in determining results.
	 */
	public Specimen Specimen;
	/**
	 * Test lab which produced this set of lab test results.
	 */
	public AssetTestLab AssetTestLab;

	public LabTestDataSet(){

	}
}//end LabTestDataSet