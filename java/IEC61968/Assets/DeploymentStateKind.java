package IEC61968.Assets;


/**
 * Possible states of asset deployment.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum DeploymentStateKind {
	notYetInstalled,
	installed,
	inService,
	outOfService,
	removed
}