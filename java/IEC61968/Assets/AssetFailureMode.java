package IEC61968.Assets;


/**
 * What asset has failed to be able to do.
 * Reason for breaker failure.
 * Note: This enumeration provides essential information to asset health analytics.
 * The existing list is a starting point and is anticipated to be fleshed out
 * further as requirements are better understood (PAB 2016/01/09).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum AssetFailureMode {
	failToCarryLoad,
	failToClose,
	failToInterrupt,
	failToOpen,
	failToProvideInsulationLevel
}