package IEC62325.InfIEC62325.InfEnergyScheduling;

import IEC61970.Base.Core.IdentifiedObject;
import IEC62325.MarketOperations.ReferenceData.SubControlArea;

/**
 * 
 * @created 03-Jan-2024 1:49:41 PM
 */
public class TieLine extends IdentifiedObject {

	/**
	 * The SubControlArea is on the A side of a collection of metered points which
	 * define the SubControlArea's boundary for a ControlAreaOperator or
	 * CustomerConsumer.
	 */
	public SubControlArea SideA_SubControlArea;
	/**
	 * The SubControlArea is on the B side of a collection of metered points which
	 * define the SubControlArea's boundary for a ControlAreaOperator or
	 * CustomerConsumer.
	 */
	public SubControlArea SideB_SubControlArea;

	public TieLine(){

	}
}//end TieLine