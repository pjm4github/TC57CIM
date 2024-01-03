package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Voltage;
import IEC61968.InfIEC61968.InfCommon.Ratio;
import IEC61968.Assets.AssetInfo;

/**
 * Properties of current transformer asset.
 * @created 29-Dec-2023 6:22:08 PM
 */
public class CurrentTransformerInfo extends AssetInfo {

	/**
	 * CT accuracy classification.
	 */
	public String accuracyClass;
	/**
	 * Accuracy limit.
	 */
	public CurrentFlow accuracyLimit;
	/**
	 * Number of cores.
	 */
	public Integer coreCount;
	public String ctClass;
	/**
	 * Maximum primary current where the CT still displays linear characteristicts.
	 */
	public CurrentFlow kneePointCurrent;
	/**
	 * Maximum voltage across the secondary terminals where the CT still displays
	 * linear characteristicts.
	 */
	public Voltage kneePointVoltage;
	/**
	 * Maximum ratio between the primary and secondary current.
	 */
	public Ratio maxRatio;
	/**
	 * Nominal ratio between the primary and secondary current; i.e. 100:5.
	 */
	public Ratio nominalRatio;
	/**
	 * Full load secondary (FLS) rating for primary winding.
	 */
	public CurrentFlow primaryFlsRating;
	/**
	 * Ratio for the primary winding tap changer.
	 */
	public Ratio primaryRatio;
	/**
	 * Rated current on the primary side.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Full load secondary (FLS) rating for secondary winding.
	 */
	public CurrentFlow secondaryFlsRating;
	/**
	 * Ratio for the secondary winding tap changer.
	 */
	public Ratio secondaryRatio;
	/**
	 * Full load secondary (FLS) rating for tertiary winding.
	 */
	public CurrentFlow tertiaryFlsRating;
	/**
	 * Ratio for the tertiary winding tap changer.
	 */
	public Ratio tertiaryRatio;
	/**
	 * Usage: eg. metering, protection, etc.
	 */
	public String usage;

	public CurrentTransformerInfo(){

	}
}//end CurrentTransformerInfo