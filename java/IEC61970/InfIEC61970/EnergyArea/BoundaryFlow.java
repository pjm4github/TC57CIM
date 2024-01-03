package IEC61970.InfIEC61970.EnergyArea;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.Terminal;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * @author selaost1
 * @version 1.0
 * @created 02-Jan-2024 11:36:32 PM
 */
public class BoundaryFlow extends IdentifiedObject {

	public Boolean positiveFlowIn;
	public EnergySchedulingAreaBoundary m_EnergySchedulingAreaBoundary;
	public Terminal m_Terminal;

	public BoundaryFlow(){

	}
}//end BoundaryFlow