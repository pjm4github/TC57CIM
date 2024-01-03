package IEC61968.InfIEC61968.InfAssets;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Hours;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Assets.Asset;

/**
 * Information regarding the experienced and expected reliability of a specific
 * asset, type of asset, or asset model.
 * @created 03-Jan-2024 12:27:03 PM
 */
public class ReliabilityInfo extends IdentifiedObject {

	/**
	 * Momentary failure rate (temporary failures/kft-year).
	 */
	public PerCent momFailureRate;
	/**
	 * Mean time to repair (MTTR - hours).
	 */
	public Hours mTTR;
	public Specification Specification;
	public Asset Assets;

	public ReliabilityInfo(){

	}
}//end ReliabilityInfo