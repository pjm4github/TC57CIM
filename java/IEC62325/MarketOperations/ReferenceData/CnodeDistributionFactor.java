package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode;

/**
 * Participation factors per Cnode.  Used to calculate "participation" of Cnode in
 * an AggregateNode. Each Cnode associated to an AggregateNode would be assigned a
 * participation factor for its participation within the AggregateNode.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class CnodeDistributionFactor extends IdentifiedObject {

	/**
	 * Used to calculate "participation" of Cnode in an AggregateNode
	 */
	public Float factor;
	/**
	 * Point of delivery loss factor
	 */
	public Float podLossFactor;
	public SubControlArea SubControlArea;
	public MktConnectivityNode MktConnectivityNode;

	public CnodeDistributionFactor(){

	}
}//end CnodeDistributionFactor