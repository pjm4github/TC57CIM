package IEC62325.MarketOperations.ReferenceData;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * Configuration Member of CCP Configuration.
 * @created 03-Jan-2024 2:15:33 PM
 */
public class CombinedCycleConfigurationMember extends IdentifiedObject {

	/**
	 * primary configuration.
	 */
	public Boolean primary;
	/**
	 * Steam plant.
	 */
	public Boolean steam;
	public MktThermalGeneratingUnit MktThermalGeneratingUnit;

	public CombinedCycleConfigurationMember(){

	}
}//end CombinedCycleConfigurationMember