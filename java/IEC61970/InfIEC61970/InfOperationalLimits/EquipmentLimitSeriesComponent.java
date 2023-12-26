package IEC61970.InfIEC61970.InfOperationalLimits;

import IEC61970.Base.Core.Equipment;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * This represents one instance of an equipment that contributes to the
 * calculation of an operational limit.
 * @author akamath
 * @version 1.0
 * @created 25-Dec-2023 8:31:56 PM
 */
public class EquipmentLimitSeriesComponent extends IdentifiedObject {

	/**
	 * Equipment contributing toward the series limit.   The reference here is to
	 * Equipment rather than a specific limit on the equipment so the grouiping can be
	 * reused for multiple limits of different types on the same instance of equipment.
	 */
	public Equipment Equipment;

	public EquipmentLimitSeriesComponent(){

	}
}//end EquipmentLimitSeriesComponent