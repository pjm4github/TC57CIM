package IEC61970.Base.SCADA;

import IEC61970.Base.Core.PowerSystemResource;
import IEC61970.Base.ICCPConfiguration.BilateralExchangeActor;

/**
 * The connection to remote units is through one or more communication links.
 * Reduntant links may exist. The CommunicationLink class inherit
 * PowerSystemResource. The intention is to allow CommunicationLinks to have
 * Measurements. These Measurements can be used to model link status as
 * operational, out of service, unit failure etc.
 * @created 07-Jan-2024 9:52:23 PM
 */
public class CommunicationLink extends PowerSystemResource {

	/**
	 * RTUs may be attached to communication links.
	 */
	public RemoteUnit RemoteUnits;
	public BilateralExchangeActor BilateralExchangeActor;

	public CommunicationLink(){

	}
}//end CommunicationLink