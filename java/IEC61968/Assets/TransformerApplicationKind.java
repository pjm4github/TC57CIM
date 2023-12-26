package IEC61968.Assets;


/**
 * Classifications of network roles in which transformers can be deployed. The
 * classifications are intended to reflect both criticality of transformer in
 * network operations and typical usage experienced by transformer.
 * Note: This enumeration provides essential information to asset health analytics.
 * The existing list is a starting point and is anticipated to be fleshed out
 * further as requirements are better understood (PAB 2016/01/09).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public enum TransformerApplicationKind {
	transmissionBusToBus,
	transmissionBusToDistribution,
	generatorStepUp,
	distribution
}