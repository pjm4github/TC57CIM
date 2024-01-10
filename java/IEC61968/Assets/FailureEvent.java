package IEC61968.Assets;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;
import IEC61968.Common.ActivityRecord;

/**
 * An event where an asset has failed to perform its functions within specified
 * parameters. This class is intended to reflect the failure itself. Additional
 * information resulting from forensic analysis could be captured by a diagnosis
 * data set.
 * @created 07-Jan-2024 9:47:25 PM
 */
public class FailureEvent extends ActivityRecord {

	/**
	 * Reason for breaker failure.
	 */
	public BreakerFailureReasonKind breakerFailureReason;
	/**
	 * Code for asset failure.
	 */
	public String corporateCode;
	/**
	 * Classification of failure.
	 */
	public AssetFailureClassification failureClassification;
	/**
	 * Time and date of asset failure.
	 */
	public DateTime failureDateTime;
	/**
	 * How the asset failure was isolated from the system.
	 */
	public FailureIsolationMethodKind failureIsolationMethod;
	/**
	 * What asset failed to be able to do.
	 */
	public AssetFailureMode failureMode;
	/**
	 * The method used for locating the faulted part of the asset. For example, cable
	 * options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection,
	 * Other.
	 */
	public String faultLocatingMethod;
	/**
	 * Failure location on an object.
	 */
	public String location;
	/**
	 * Root cause of asset failure.
	 */
	public String rootCause;
	/**
	 * Reason for transformer failure.
	 */
	public TransformerFailureReasonKind transformerFailureReason;

	public FailureEvent(){

	}
}//end FailureEvent