package IEC61968.InfIEC61968.InfAssetInfo;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Core.PhaseCode;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Voltage;
import IEC61968.Assets.AssetInfo;

/**
 * Properties of a composite switch.
 * @created 29-Dec-2023 6:21:55 PM
 */
public class CompositeSwitchInfo extends AssetInfo {

	/**
	 * True if multi-phase switch controls all phases concurrently.
	 */
	public Boolean ganged;
	/**
	 * Initial operating mode, with the following values: Automatic, Manual.
	 */
	public String initOpMode;
	/**
	 * Breaking capacity, or short circuit rating, is the maximum rated current which
	 * the device can safely interrupt at the rated voltage.
	 */
	public CurrentFlow interruptingRating;
	/**
	 * Kind of composite switch.
	 */
	public CompositeSwitchKind kind;
	/**
	 * Phases carried, if applicable.
	 */
	public PhaseCode phaseCode;
	/**
	 * Supported number of phases, typically 0, 1 or 3.
	 */
	public Integer phaseCount;
	/**
	 * Rated voltage.
	 */
	public Voltage ratedVoltage;
	/**
	 * True if device is capable of being operated by remote control.
	 */
	public Boolean remote;
	/**
	 * Number of switch states represented by the composite switch.
	 */
	public Integer switchStateCount;

	public CompositeSwitchInfo(){

	}
}//end CompositeSwitchInfo