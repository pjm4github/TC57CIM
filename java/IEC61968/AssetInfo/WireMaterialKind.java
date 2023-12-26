package IEC61968.AssetInfo;


/**
 * Kind of wire material.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:26 PM
 */
public enum WireMaterialKind {
	/**
	 * Copper wire.
	 */
	copper,
	/**
	 * Steel wire.
	 */
	steel,
	/**
	 * Aluminum wire.
	 */
	aluminum,
	/**
	 * Aluminum-steel wire.
	 */
	aluminumSteel,
	/**
	 * Aluminum conductor steel reinforced.
	 */
	acsr,
	/**
	 * Aluminum-alloy wire.
	 */
	aluminumAlloy,
	/**
	 * Aluminum-alloy-steel wire.
	 */
	aluminumAlloySteel,
	/**
	 * Aluminum-alloy conductor steel reinforced.
	 */
	aaac,
	/**
	 * Other wire material.
	 */
	other
}