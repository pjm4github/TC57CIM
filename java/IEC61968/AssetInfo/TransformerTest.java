package IEC61968.AssetInfo;

import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.Temperature;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Test result for transformer ends, such as short-circuit, open-circuit
 * (excitation) or no-load test.
 * @author Tom
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class TransformerTest extends IdentifiedObject {

	/**
	 * Base power at which the tests are conducted, usually equal to the rateds of one
	 * of the involved transformer ends.
	 */
	public ApparentPower basePower;
	/**
	 * Temperature at which the test is conducted.
	 */
	public Temperature temperature;

	public TransformerTest(){

	}
}//end TransformerTest