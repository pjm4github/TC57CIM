package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.InterTieDirection;
import IEC62325.MarketOperations.MktDomain.EnergyProductType;
import IEC62325.MarketOperations.MktDomain.YesNo;
import IEC61970.Base.Domain.Integer;
import IEC62325.MarketOperations.ParticipantInterfaces.InterTieDispatchResponse;
import IEC62325.MarketCommon.RegisteredResource;

/**
 * This class represents the inter tie resource.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class RegisteredInterTie extends RegisteredResource {

	/**
	 * Indicates the direction (export/import) of an InterTie resource.
	 */
	public InterTieDirection direction;
	/**
	 * Under each major product type, the commodity type can be applied to further
	 * specify the type.
	 */
	public EnergyProductType energyProductType;
	/**
	 * Flag to indicated whether this Inter-tie is a DC Tie.
	 */
	public YesNo isDCTie;
	/**
	 * Specifies whether the inter-tie resource is registered for the dynamic
	 * interchange.
	 */
	public YesNo isDynamicInterchange;
	/**
	 * The registered upper bound of minimum hourly block for an Inter-Tie Resource.
	 */
	public Integer minHourlyBlockLimit;
	public InterTieDispatchResponse InterTieDispatchResponse;

	public RegisteredInterTie(){

	}
}//end RegisteredInterTie