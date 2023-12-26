package IEC61968.AssetInfo;

import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Pressure;
import IEC61970.Base.Domain.Volume;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Seconds;
import IEC61968.Assets.AssetInfo;

/**
 * <was Switch data.>
 * Switch datasheet information.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:25 PM
 */
public class SwitchInfo extends AssetInfo {

	/**
	 * The maximum fault current a breaking device can break safely under prescribed
	 * conditions of use.
	 */
	public CurrentFlow breakingCapacity;
	/**
	 * Weight of gas in each tank of SF<sub>6</sub> dead tank breaker.
	 */
	public Mass gasWeightPerTank;
	/**
	 * If true, it is a single phase switch.
	 */
	public Boolean isSinglePhase;
	/**
	 * If true, the switch is not ganged (i.e., a switch phase may be operated
	 * separately from other phases).
	 */
	public Boolean isUnganged;
	/**
	 * Gas or air pressure at or below which a low pressure alarm is generated.
	 */
	public Pressure lowPressureAlarm;
	/**
	 * Gas or air pressure below which the breaker will not open.
	 */
	public Pressure lowPressureLockOut;
	/**
	 * Volume of oil in each tank of bulk oil breaker.
	 */
	public Volume oilVolumePerTank;
	/**
	 * Rated current.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Frequency for which switch is rated.
	 */
	public Frequency ratedFrequency;
	/**
	 * Rated impulse withstand voltage, also known as BIL (Basic Impulse Level).
	 */
	public Voltage ratedImpulseWithstandVoltage;
	/**
	 * Switch rated interrupting time in seconds.
	 */
	public Seconds ratedInterruptingTime;
	/**
	 * Rated voltage.
	 */
	public Voltage ratedVoltage;

	public SwitchInfo(){

	}
}//end SwitchInfo