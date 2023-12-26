package IEC61968.Assets;


/**
 * Type of hazard that is posed to asset in this location.
 * Note: This enumeration provides essential information to asset health analytics.
 * The existing list is a starting point and is anticipated to be fleshed out
 * further as requirements are better understood (PAB 2016/01/09).
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum AssetHazardKind {
	/**
	 * Subject to ambient temperature of below -12 øC.
	 */
	ambientTempBelowMinus12,
	/**
	 * Subject to ambient temperature above 38 øC.
	 */
	ambientTempAbove38,
	/**
	 * Vegetation growing below asset that may cause problem.
	 */
	vegetation,
	/**
	 * Children play in area (stray kite/ball hazard).
	 */
	childrenAtPlay,
	/**
	 * Fishing in area (fishing pole/line hazard).
	 */
	fishingArea,
	/**
	 * If other, look at type field for more information.
	 */
	other
}