package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC61970.Base.Core.PowerSystemResource;

/**
 * A corridor containing one or more rights of way
 * @created 03-Jan-2024 1:49:41 PM
 */
public class TransmissionCorridor extends PowerSystemResource {

	/**
	 * A transmission right-of-way is a member of a transmission corridor
	 */
	public TransmissionRightOfWay TransmissionRightOfWays;

	public TransmissionCorridor(){

	}
}//end TransmissionCorridor