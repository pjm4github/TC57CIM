package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * Test results, usually obtained by a lab or other independent organisation.
 * @created 07-Jan-2024 9:49:12 PM
 */
public class TestDataSet extends ProcedureDataSet {

	/**
	 * Conclusion drawn from test results.
	 */
	public String conclusion;
	/**
	 * Identifier of specimen used in inspection or test.
	 */
	public String specimenID;
	/**
	 * Date and time the specimen was received by the lab.
	 */
	public DateTime specimenToLabDateTime;

	public TestDataSet(){

	}
}//end TestDataSet