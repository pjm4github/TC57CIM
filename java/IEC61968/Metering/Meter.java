package IEC61968.Metering;

import IEC61970.Base.Domain.String;

/**
 * Physical asset that performs the metering role of the usage point. Used for
 * measuring consumption and detection of events.
 * @created 25-Dec-2023 8:45:22 PM
 */
public class Meter extends EndDevice {

	/**
	 * Meter form designation per ANSI C12.10 or other applicable standard. An
	 * alphanumeric designation denoting the circuit arrangement for which the meter
	 * is applicable and its specific terminal arrangement.
	 */
	public String formNumber;
	/**
	 * All multipliers applied at this meter.
	 */
	public MeterMultiplier MeterMultipliers;
	/**
	 * All meter readings provided by this meter.
	 */
	public MeterReading MeterReadings;

	public Meter(){

	}
}//end Meter