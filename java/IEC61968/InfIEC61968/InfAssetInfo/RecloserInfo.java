package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Integer;

/**
 * Properties of recloser assets.
 * @created 29-Dec-2023 6:23:14 PM
 */
public class RecloserInfo extends OldSwitchInfo {

	/**
	 * True if device has ground trip capability.
	 */
	public Boolean groundTripCapable;
	/**
	 * True if normal status of ground trip is enabled.
	 */
	public Boolean groundTripNormalEnabled;
	/**
	 * Ground trip rating.
	 */
	public CurrentFlow groundTripRating;
	/**
	 * Phase trip rating.
	 */
	public CurrentFlow phaseTripRating;
	/**
	 * Total number of phase reclose operations.
	 */
	public Integer recloseLockoutCount;

	public RecloserInfo(){

	}
}//end RecloserInfo