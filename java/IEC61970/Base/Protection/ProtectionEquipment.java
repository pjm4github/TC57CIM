package IEC61970.Base.Protection;

import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Domain.UnitMultiplier;
import IEC61970.Base.Domain.UnitSymbol;
import IEC61970.Base.Wires.ProtectedSwitch;
import IEC61970.Base.Core.Equipment;
import IEC61970.Base.Core.ConductingEquipment;
import IEC61970.InfIEC61970.InfSIPS.ProtectiveAction;

/**
 * An electrical device designed to respond to input conditions in a prescribed
 * manner and after specified conditions are met to cause contact operation or
 * similar abrupt change in associated electric control circuits, or simply to
 * display the detected condition. Protection equipment are associated with
 * conducting equipment and usually operate circuit breakers.
 * @created 25-Dec-2023 8:32:02 PM
 */
public class ProtectionEquipment extends Equipment {

	/**
	 * The maximum allowable value.
	 */
	public Float highLimit;
	/**
	 * The minimum allowable value.
	 */
	public Float lowLimit;
	/**
	 * Direction same as positive active power flow value.
	 */
	public Boolean powerDirectionFlag;
	/**
	 * The time delay from detection of abnormal conditions to relay operation.
	 */
	public Seconds relayDelayTime;
	/**
	 * The unit multiplier of the value.
	 */
	public UnitMultiplier unitMultiplier;
	/**
	 * The unit of measure of the value.
	 */
	public UnitSymbol unitSymbol;
	/**
	 * Protected switches operated by this ProtectionEquipment.
	 */
	public ProtectedSwitch ProtectedSwitches;
	/**
	 * Protection equipment may be used to protect specific conducting equipment.
	 */
	public ConductingEquipment ConductingEquipments;
	public ProtectiveAction ProtectiveAction;

	public ProtectionEquipment(){

	}
}//end ProtectionEquipment