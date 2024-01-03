package IEC61970.Base.Equivalents;

import IEC61970.Base.Core.ConnectivityNodeContainer;

/**
 * A class that represents an external meshed network that has been reduced to an
 * electrically equivalent model. The ConnectivityNodes contained in the
 * equivalent are intended to reflect internal nodes of the equivalent. The
 * boundary Connectivity nodes where the equivalent connects outside itself are
 * NOT contained by the equivalent.
 * @created 02-Jan-2024 10:46:32 PM
 */
public class EquivalentNetwork extends ConnectivityNodeContainer {

	/**
	 * The associated reduced equivalents.
	 */
	public EquivalentEquipment EquivalentEquipments;

	public EquivalentNetwork(){

	}
}//end EquivalentNetwork