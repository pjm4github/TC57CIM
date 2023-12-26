package IEC61968.Assets;


/**
 * Reason for transformer failure.
 * Note: This enumeration provides essential information to asset health analytics.
 * The existing list is a starting point and is anticipated to be fleshed out
 * further as requirements are better understood (PAB 2016/01/09).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum TransformerFailureReasonKind {
	bushingFailure,
	lossOfOil,
	oilRelatedFailure,
	poorOilQuality
}