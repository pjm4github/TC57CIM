package IEC61968.AssetInfo;

import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.ReactivePower;
import IEC61970.Base.Domain.Voltage;
import IEC61968.InfIEC61968.InfWiresExt.ShuntCompensatorControl;
import IEC61968.Assets.AssetInfo;

/**
 * Properties of shunt capacitor, shunt reactor or switchable bank of shunt
 * capacitor or reactor assets.
 * @created 29-Dec-2023 5:38:48 PM
 */
public class ShuntCompensatorInfo extends AssetInfo {

	/**
	 * Maximum allowed apparent power loss.
	 */
	public ApparentPower maxPowerLoss;
	/**
	 * Rated current.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Rated reactive power.
	 */
	public ReactivePower ratedReactivePower;
	/**
	 * Rated voltage.
	 */
	public Voltage ratedVoltage;
	public ShuntCompensatorControl ShuntCompensatorControl;

	public ShuntCompensatorInfo(){

	}
}//end ShuntCompensatorInfo