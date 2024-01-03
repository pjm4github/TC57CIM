# package IEC61968.Assets;
#
# import IEC61970.Base.Domain.String;
# import IEC61970.Base.Domain.DateTime;
# import IEC61968.Common.ActivityRecord;
#
# /**
#  * An event where an asset has failed to perform its functions within specified
#  * parameters. This class is intended to reflect the failure itself. Additional
#  * information resulting from forensic analysis could be captured by a diagnosis
#  * data set.
#  * @created 29-Dec-2023 5:26:43 PM
#  */
# public class FailureEvent extends ActivityRecord {
#
# 	/**
# 	 * Reason for breaker failure.
# 	 */
# 	public BreakerFailureReasonKind breakerFailureReason;
# 	/**
# 	 * Code for asset failure.
# 	 */
# 	public String corporateCode;
# 	/**
# 	 * Classification of failure.
# 	 */
# 	public AssetFailureClassification failureClassification;
# 	/**
# 	 * Time and date of asset failure.
# 	 */
# 	public DateTime failureDateTime;
# 	/**
# 	 * How the asset failure was isolated from the system.
# 	 */
# 	public FailureIsolationMethodKind failureIsolationMethod;
# 	/**
# 	 * What asset failed to be able to do.
# 	 */
# 	public AssetFailureMode failureMode;
# 	/**
# 	 * The method used for locating the faulted part of the asset. For example, cable
# 	 * options include: Cap Discharge-Thumping, Bridge Method, Visual Inspection,
# 	 * Other.
# 	 */
# 	public String faultLocatingMethod;
# 	/**
# 	 * Failure location on an object.
# 	 */
# 	public String location;
# 	/**
# 	 * Root cause of asset failure.
# 	 */
# 	public String rootCause;
# 	/**
# 	 * Reason for transformer failure.
# 	 */
# 	public TransformerFailureReasonKind transformerFailureReason;
#
# 	public FailureEvent(){
#
# 	}
# }//end FailureEvent
from IEC61968.Assets.AssetFailureClassification import AssetFailureClassification
from IEC61968.Assets.AssetFailureMode import AssetFailureMode
from IEC61968.Assets.BreakerFailureReasonKind import BreakerFailureReasonKind
from IEC61968.Assets.FailureIsolationMethodKind import FailureIsolationMethodKind
from IEC61968.Assets.TransformerFailureReasonKind import TransformerFailureReasonKind
from IEC61968.Common.ActivityRecord import ActivityRecord
from IEC61970.Base.Domain.DateTime import DateTime


class FailureEvent(ActivityRecord):
    def __init__(self):
        super().__init__()
        self.breaker_failure_reason = BreakerFailureReasonKind.BUSHING_FAILURE  # Reason for breaker failure
        self.corporate_code = ""  # Code for asset failure
        self.failure_classification = AssetFailureClassification.MINOR  # Classification of failure
        self.failure_date_time = DateTime()  # Time and date of asset failure
        self.failure_isolation_method = FailureIsolationMethodKind.MANUALLY_ISOLATED  # How the asset failure was isolated from the system
        self.failure_mode = AssetFailureMode.FAIL_TO_OPEN # What asset failed to be able to do
        self.fault_locating_method = ""  # The method used for locating the faulted part of the asset
        self.location = ""  # Failure location on an object
        self.root_cause = ""  # Root cause of asset failure
        self.transformer_failure_reason = TransformerFailureReasonKind.BUSHING_FAILURE  # Reason for transformer failure
