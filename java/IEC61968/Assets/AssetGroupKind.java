package IEC61968.Assets;

import IEC61970.Base.Domain.DateTime;

/**
 * Possible kinds of asset groups.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public enum AssetGroupKind {
	analysisGroup,
	inventoryGroup,
	complianceGroup,
	/**
	 * assets grouped together for a particular function - such as a group of feeders.
	 */
	functionalGroup,
	other
}