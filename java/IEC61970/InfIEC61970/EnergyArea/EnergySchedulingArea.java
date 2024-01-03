package IEC61970.InfIEC61970.EnergyArea;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * @author selaost1
 * @version 1.0
 * @created 02-Jan-2024 11:37:12 PM
 */
public class EnergySchedulingArea extends PowerSystemResource {

	public ActivePower netACInterchange;
	public Float netACInterchangeTolerance;
	public EnergyAreaTypeKind type;
	public EnergySchedulingAreaBoundary m_EnergySchedulingAreaBoundary;

	public EnergySchedulingArea(){

	}
}//end EnergySchedulingArea