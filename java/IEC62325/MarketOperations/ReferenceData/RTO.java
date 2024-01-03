package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MarketPlan.CommodityDefinition;
import IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode;
import IEC62325.MarketCommon.MarketParticipant;

/**
 * Regional transmission operator.
 * @created 03-Jan-2024 2:15:34 PM
 */
public class RTO extends MarketParticipant {

	public AdjacentCASet AdjacentCASet;
	public LocalReliabilityArea LocalReliabilityArea;
	public FuelRegion FuelRegion;
	public ContractRight TransmissionContractRight;
	public AggregateNode AggregateNode;
	public HostControlArea HostControlArea;
	public Pnode Pnodes;
	public TransmissionRightChain TransmissionRightChain;
	public SubControlArea SubControlArea;
	public CommodityDefinition CommodityDefinition;
	public MktConnectivityNode MktConnectivityNode;

	public RTO(){

	}
}//end RTO