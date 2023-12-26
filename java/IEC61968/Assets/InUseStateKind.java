package IEC61968.Assets;


/**
 * Possible 'in use' states that an asset can be in.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public enum InUseStateKind {
	/**
	 * Asset is deployed (in use) or is being put into use.
	 */
	inUse,
	/**
	 * Asset is ready to be put into use.
	 */
	readyForUse,
	/**
	 * Asset is not ready to be put into use.
	 */
	notReadyForUse
}