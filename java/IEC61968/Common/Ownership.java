package IEC61968.Common;

import IEC61970.Base.Domain.PerCent;
import IEC61968.Assets.Asset;
import IEC61968.Assets.AssetOwner;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Ownership of e.g. asset.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class Ownership extends IdentifiedObject {

	/**
	 * Share of this ownership.
	 */
	public PerCent share;
	/**
	 * Asset that is object of this ownership.
	 */
	public Asset Asset;
	/**
	 * Asset owner that is subject in this ownership.
	 */
	public AssetOwner AssetOwner;

	public Ownership(){

	}
}//end Ownership