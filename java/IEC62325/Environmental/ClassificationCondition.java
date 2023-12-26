package IEC62325.Environmental;

import IEC61970.Base.Domain.Seconds;
import IEC62325.Environmental.EnvDomain.TestKind;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A classification condition used to define preconditions that must be met by a
 * phenomena classification.
 * @author mcmorran
 * @version 1.0
 * @created 25-Dec-2023 8:48:36 PM
 */
public class ClassificationCondition extends IdentifiedObject {

	/**
	 * The duration of the of the condition in seconds
	 */
	public Seconds duration;
	/**
	 * The test applied to the value.
	 */
	public TestKind test;
	/**
	 * Phenomenon classification to which this condition relates.
	 */
	public PhenomenonClassification PhenomenonClassification;

	public ClassificationCondition(){

	}
}//end ClassificationCondition