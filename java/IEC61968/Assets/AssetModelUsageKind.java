package IEC61968.Assets;


/**
 * Usage for an asset model.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum AssetModelUsageKind {
	/**
	 * Asset model is intended for use in distribution overhead network.
	 */
	distributionOverhead,
	/**
	 * Asset model is intended for use in underground distribution network.
	 */
	distributionUnderground,
	/**
	 * Asset model is intended for use in transmission network.
	 */
	transmission,
	/**
	 * Asset model is intended for use in substation.
	 */
	substation,
	/**
	 * Asset model is intended for use as streetlight.
	 */
	streetlight,
	/**
	 * Asset model is intended for use in customer substation.
	 */
	customerSubstation,
	/**
	 * Usage of the asset model is unknown.
	 */
	unknown,
	/**
	 * Other kind of asset model usage.
	 */
	other
}