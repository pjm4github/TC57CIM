package IEC61970.Base.SCADA;

import IEC61970.Base.Core.PowerSystemResource;

/**
 * A remote unit can be a RTU, IED, substation control system, control center etc.
 * The communication with the remote unit can be through various standard
 * protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP,
 * RP570 etc.). A remote unit contain remote data points that might be telemetered,
 * collected or calculated. The RemoteUnit class inherit PowerSystemResource. The
 * intention is to allow RemotUnits to have Measurements. These Measurements can
 * be used to model unit status as operational, out of service, unit failure etc.
 * @created 02-Jan-2024 11:30:20 PM
 */
public class RemoteUnit extends PowerSystemResource {

	/**
	 * Type of remote unit.
	 */
	public RemoteUnitType remoteUnitType;
	/**
	 * Remote points this Remote unit contains.
	 */
	public RemotePoint RemotePoints;

	public RemoteUnit(){

	}
}//end RemoteUnit