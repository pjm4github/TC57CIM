package IEC61968.AssetInfo;

import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Voltage;
import IEC61968.Assets.AssetInfo;

/**
 * Breaker operating mechanism datasheet information.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:23 PM
 */
public class OperatingMechanismInfo extends AssetInfo {

	/**
	 * Close current (nominal).
	 */
	public CurrentFlow closeAmps;
	/**
	 * Close voltage in volts DC.
	 */
	public Voltage closeVoltage;
	/**
	 * Kind of breaker operating mechanism.
	 */
	public OperatingMechanismKind mechanismKind;
	/**
	 * Rated motor run current in amps.
	 */
	public CurrentFlow motorRunCurrent;
	/**
	 * Rated motor start current in amps.
	 */
	public CurrentFlow motorStartCurrent;
	/**
	 * Nominal motor voltage in volts DC.
	 */
	public Voltage motorVoltage;
	/**
	 * Trip current (nominal).
	 */
	public CurrentFlow tripAmps;
	/**
	 * Trip voltage in volts DC.
	 */
	public Voltage tripVoltage;

	public OperatingMechanismInfo(){

	}
}//end OperatingMechanismInfo