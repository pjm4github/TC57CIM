package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;

/**
 * Optimal Power Flow or State Estimator Phase Shifter Data. This is used for
 * RealTime, Study and Maintenance Users. SE Solution Phase Shifter Measurements
 * from the last run of SE.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class TapChangerDynamicData {

	/**
	 * True means the phase shifter is regulating.
	 */
	public Boolean angleRegulationStatus;
	/**
	 * Phase Shifter Desired MW. The active power regulation setpoint of the phase
	 * shifter
	 */
	public Float desiredMW;
	/**
	 * The desired voltage for the LTC
	 */
	public Float desiredVoltage;
	/**
	 * The maximum phase angle shift of the phase shifter
	 */
	public Float maximumAngle;
	/**
	 * The minimum phase angle shift of the phase shifter
	 */
	public Float minimumAngle;
	/**
	 * Phase Shifter Angle. The solved phase angle shift of the phase shifter
	 */
	public Float solvedAngle;
	/**
	 * Tap position of the phase shifter, high-side tap position of the transformer,
	 * or  low-side tap position of the transformer
	 */
	public Float tapPosition;
	/**
	 * Indicator if the LTC transformer is regulating True = Yes, False = No
	 */
	public Boolean voltageRegulationStatus;
	public MktTapChanger MktTapChanger;

	public TapChangerDynamicData(){

	}
}//end TapChangerDynamicData