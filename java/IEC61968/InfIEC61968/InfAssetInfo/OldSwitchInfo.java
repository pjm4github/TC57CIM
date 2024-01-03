package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Integer;
import IEC61968.AssetInfo.SwitchInfo;

/**
 * Properties of switch assets.
 * @created 29-Dec-2023 6:23:45 PM
 */
public class OldSwitchInfo extends SwitchInfo {

	/**
	 * The maximum rms voltage that may be applied across an open contact without
	 * breaking down the dielectric properties of the switch in the open position.
	 */
	public Voltage dielectricStrength;
	/**
	 * True if switch has load breaking capabiity. Unless specified false, this is
	 * always assumed to be true for breakers and reclosers.
	 */
	public Boolean loadBreak;
	/**
	 * The highest value of current the switch can make at the rated voltage under
	 * specified operating conditions without suffering significant deterioration of
	 * its performance.
	 */
	public CurrentFlow makingCapacity;
	/**
	 * The lowest value of current that the switch can make, carry and break in
	 * uninterrupted duty at the rated voltage under specified operating conditions
	 * without suffering significant deterioration of its performance.
	 */
	public CurrentFlow minimumCurrent;
	/**
	 * Number of poles (i.e. of current carrying conductors that are switched).
	 */
	public Integer poleCount;
	/**
	 * True if device is capable of being operated by remote control.
	 */
	public Boolean remote;
	/**
	 * The highest value of current the switch can carry in the closed position at the
	 * rated voltage under specified operating conditions without suffering
	 * significant deterioration of its performance.
	 */
	public CurrentFlow withstandCurrent;

	public OldSwitchInfo(){

	}
}//end OldSwitchInfo