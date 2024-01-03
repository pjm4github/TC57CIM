package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.DC.DCConductingEquipment;

/**
 * Protective actions on non-switching equipment. The operating condition is
 * adjusted.
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:33:30 PM
 */
public class ProtectiveActionAdjustment extends ProtectiveAction {

	/**
	 * The adjustment is given in percent of the active value.
	 */
	public PerCent byPercentage;
	/**
	 * The adjustment is given in value of the active value.
	 */
	public Float byValue;
	/**
	 * Defines the kind of adjustment that should be done. With this value the correct
	 * attribute containing the value needs to be used.
	 */
	public ProtectiveActionAdjustmentKind kind;
	/**
	 * If true, the adjusted value is an reduction. Other wise it is an increase in
	 * the value.
	 */
	public Boolean reduce;
	/**
	 * The adjustment is given by a new active value.
	 */
	public Float setValue;
	public DCConductingEquipment DCConductingEquipment;

	public ProtectiveActionAdjustment(){

	}
}//end ProtectiveActionAdjustment