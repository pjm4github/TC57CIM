package IEC62325.MarketOperations.ReferenceData;

import IEC62325.MarketOperations.MktDomain.AnodeType;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * An aggregated node can define a typed grouping further defined by the AnodeType
 * enumeratuion. Types range from System Zone/Regions to Market Energy Regions to
 * Aggregated Loads and Aggregated Generators.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class AggregateNode extends IdentifiedObject {

	/**
	 * Type of aggregated node
	 */
	public AnodeType anodeType;
	/**
	 * Processing Order for AS self-provisions for this region. The priority of this
	 * attribute directs the awards of any resource that resides in overlapping
	 * regions. The regions are processed in priority manner.
	 */
	public Integer qualifASOrder;
	public Pnode Pnode;
	public CnodeDistributionFactor CnodeDistributionFactor;
	public SubControlArea SubControlArea;

	public AggregateNode(){

	}
}//end AggregateNode