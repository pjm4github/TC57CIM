package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;

/**
 * Optimal Power Flow or State Estimator Filter Bank Data for OTS. This is used
 * for RealTime, Study and Maintenance Users.
 * @created 03-Jan-2024 2:08:11 PM
 */
public class ShuntCompensatorDynamicData {

	/**
	 * The current status for the Voltage Control Capacitor 1= Connected 0 =
	 * Disconnected
	 */
	public Integer connectionStatus;
	/**
	 * The desired voltage for the Voltage Control Capacitor
	 */
	public Float desiredVoltage;
	/**
	 * The injection of reactive power of the filter bank in the NA solution or VCS
	 * reactive power production
	 */
	public Float mVARInjection;
	/**
	 * Voltage control capacitor step position
	 */
	public Integer stepPosition;
	/**
	 * Indicator if the voltage control this is regulating True = Yes, False = No
	 */
	public Boolean voltageRegulationStatus;
	public MktShuntCompensator MktShuntCompensator;

	public ShuntCompensatorDynamicData(){

	}
}//end ShuntCompensatorDynamicData