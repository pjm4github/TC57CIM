package IEC61968.Assets;


/**
 * Lifecycle states an asset can be in.
 * While the possible lifecycle states are standardized, the allowed transitions
 * are not - they are intended to be defined by the business process requirements
 * of local implementations.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum AssetLifecycleStateKind {
	manufactured,
	purchased,
	received,
	retired,
	disposedOf
}