package IEC61970.InfIEC61970.EnergyArea;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * @author selaost1
 * @version 1.0
 * @created 02-Jan-2024 11:35:12 PM
 */
public class EnergyGroup extends PowerSystemResource {

	public Boolean isSlack;
	public ActivePower p;
	public EnergyTypeReference m_EnergyTypeReference;
	public EnergySchedulingArea m_EnergySchedulingArea;

	public EnergyGroup(){

	}
}//end EnergyGroup