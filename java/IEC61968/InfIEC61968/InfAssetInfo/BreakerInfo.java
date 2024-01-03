package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.CurrentFlow;

/**
 * Properties of breaker assets.
 * @created 29-Dec-2023 6:21:42 PM
 */
public class BreakerInfo extends OldSwitchInfo {

	/**
	 * Phase trip rating.
	 */
	public CurrentFlow phaseTrip;

	public BreakerInfo(){

	}
}//end BreakerInfo