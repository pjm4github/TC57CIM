package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.ActivePower;
import IEC62325.MarketOperations.ReferenceData.SubControlArea;

/**
 * The control area's reserve specification.
 * @created 03-Jan-2024 1:49:41 PM
 */
public class AreaReserveSpec {

	/**
	 * Description of the object or instance.
	 */
	public String Description;
	/**
	 * Lower regulating margin requirement in MW, the amount of generation that can be
	 * dropped by control in 10 minutes
	 */
	public ActivePower lowerRegMarginReqt;
	/**
	 * Operating reserve requirement in MW, where operating reserve is the generating
	 * capability that is fully available within 30 minutes. Operating reserve is
	 * composed of primary reserve (t less than 10 min) and secondary reserve (10 less
	 * than t less than 30 min).
	 */
	public ActivePower opReserveReqt;
	/**
	 * Primary reserve requirement in MW, where primary reserve is generating
	 * capability that is fully available within 10 minutes. Primary reserve is
	 * composed of spinning reserve and quick-start reserve.
	 */
	public ActivePower primaryReserveReqt;
	/**
	 * Raise regulating margin requirement in MW, the amount of generation that can be
	 * picked up by control in 10 minutes
	 */
	public ActivePower raiseRegMarginReqt;
	/**
	 * Spinning reserve requirement in MW, spinning reserve is generating capability
	 * that is presently synchronized to the network and is fully available within 10
	 * minutes
	 */
	public ActivePower spinningReserveReqt;
	public SubControlArea SubControlArea;

	public AreaReserveSpec(){

	}
}//end AreaReserveSpec