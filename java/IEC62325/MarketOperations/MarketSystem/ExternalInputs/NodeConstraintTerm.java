package IEC62325.MarketOperations.MarketSystem.ExternalInputs;

import IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode;

/**
 * To be used only to constrain a quantity that cannot be associated with a
 * terminal. For example, a registered generating unit that is not electrically
 * connected to the network.
 * @created 03-Jan-2024 2:08:10 PM
 */
public class NodeConstraintTerm extends ConstraintTerm {

	public MktConnectivityNode MktConnectivityNode;

	public NodeConstraintTerm(){

	}
}//end NodeConstraintTerm