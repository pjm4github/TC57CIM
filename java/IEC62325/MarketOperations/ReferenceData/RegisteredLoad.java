package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Boolean;
import IEC62325.MarketOperations.ParticipantInterfaces.LoadBid;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * Model of a load that is registered to participate in the market.
 * 
 * RegisteredLoad is used to model any load that is served by the wholesale market
 * directly. RegisteredLoads may be dispatchable or non-dispatchable and may or
 * may not have bid curves. Examples of RegisteredLoads would include:
 * distribution company load, energy retailer load, large bulk power system
 * connected facility load.
 * 
 * Loads that are served indirectly, for example - through an energy retailer or a
 * vertical utility, should be modeled as RegisteredDistributedResources. Examples
 * of RegisteredDistributedResources would include: distribution level storage,
 * distribution level generation and distribution level demand response.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class RegisteredLoad extends RegisteredResource {

	/**
	 * Emergency operating procedure - Flag to indicate that the Resource is Block
	 * Load pseudo resource.
	 */
	public Boolean blockLoadTransfer;
	/**
	 * Flag to indicate that a Load Resource is part of a DSR Load
	 */
	public Boolean dynamicallyScheduledLoadResource;
	/**
	 * Qualification status (used for DSR qualification).
	 */
	public Boolean dynamicallyScheduledQualification;
	public LoadBid LoadBids;

	public RegisteredLoad(){

	}
}//end RegisteredLoad