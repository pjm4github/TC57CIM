package IEC61970.InfIEC61970.EnergyArea;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * @author selaost1
 * @version 1.0
 * @created 02-Jan-2024 11:35:52 PM
 */
public class BlockDispatchOrder extends IdentifiedObject {

	public ActivePower p;
	public Integer sequence;
	public BlockDispatchComponent m_BlockDispatchComponent;

	public BlockDispatchOrder(){

	}
}//end BlockDispatchOrder