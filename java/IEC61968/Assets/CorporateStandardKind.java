package IEC61968.Assets;


/**
 * Kind of corporate standard.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:20 PM
 */
public enum CorporateStandardKind {
	/**
	 * Asset model is used as corporate standard.
	 */
	standard,
	/**
	 * Asset model is used experimentally.
	 */
	experimental,
	/**
	 * Asset model usage is under evaluation.
	 */
	underEvaluation,
	/**
	 * Other kind of corporate standard for the asset model.
	 */
	other
}