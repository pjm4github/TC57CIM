package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.ApparentPower;
import IEC61968.AssetInfo.TransformerEndInfo;

/**
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OldTransformerEndInfo extends TransformerEndInfo {

	/**
	 * Overload rating for 24 hours.
	 */
	public ApparentPower dayOverLoadRating;
	/**
	 * Overload rating for 1 hour.
	 */
	public ApparentPower hourOverLoadRating;
	/**
	 * Weight of solid insultation in transformer.
	 */
	public Mass solidInsulationWeight;
	/**
	 * Type of insultation used for transformer windings.
	 */
	public WindingInsulationKind windingInsulationKind;

	public OldTransformerEndInfo(){

	}
}//end OldTransformerEndInfo