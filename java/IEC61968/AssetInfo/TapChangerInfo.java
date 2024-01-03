package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Frequency;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ApparentPower;
import IEC61970.Base.Domain.AngleDegrees;
import IEC61970.Base.Domain.PerCent;
import IEC61968.Assets.AssetInfo;

/**
 * Tap changer data.
 * @created 29-Dec-2023 5:39:09 PM
 */
public class TapChangerInfo extends AssetInfo {

	/**
	 * Basic Insulation Level (BIL) expressed as the impulse crest voltage of a
	 * nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability
	 * of the insulation to withstand very high voltage surges.
	 */
	public Voltage bil;
	/**
	 * Built-in current transformer primary rating.
	 */
	public CurrentFlow ctRating;
	/**
	 * Built-in current transducer ratio.
	 */
	public Float ctRatio;
	/**
	 * Frequency at which the ratings apply.
	 */
	public Frequency frequency;
	/**
	 * Highest possible tap step position, advance from neutral.
	 */
	public Integer highStep;
	/**
	 * Whether this tap changer has under load tap changing capabilities.
	 */
	public Boolean isTcul;
	/**
	 * Lowest possible tap step position, retard from neutral.
	 */
	public Integer lowStep;
	/**
	 * The neutral tap step position for the winding.
	 */
	public Integer neutralStep;
	/**
	 * Voltage at which the winding operates at the neutral tap setting.
	 */
	public Voltage neutralU;
	/**
	 * Built-in voltage transducer ratio.
	 */
	public Float ptRatio;
	/**
	 * Rated apparent power.
	 */
	public ApparentPower ratedApparentPower;
	/**
	 * Rated current.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Rated voltage.
	 */
	public Voltage ratedVoltage;
	/**
	 * Phase shift per step position.
	 */
	public AngleDegrees stepPhaseIncrement;
	/**
	 * Tap step increment, in per cent of rated voltage, per step position.
	 */
	public PerCent stepVoltageIncrement;

	public TapChangerInfo(){

	}
}//end TapChangerInfo