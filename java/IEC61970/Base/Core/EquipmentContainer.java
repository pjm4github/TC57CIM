package IEC61970.Base.Core;


/**
 * A modeling construct to provide a root class for containing equipment.
 * @created 02-Jan-2024 10:33:51 PM
 */
public class EquipmentContainer extends ConnectivityNodeContainer {

	/**
	 * Contained equipment.
	 */
	public Equipment Equipments;
	/**
	 * The additonal contained equipment.  The equipment belong to the equipment
	 * container. The equipment is contained in another equipment container, but also
	 * grouped with this equipment container.  Examples include when a switch
	 * contained in a substation is also desired to be grouped with a line contianer
	 * or when a switch is included in a secondary substation and also grouped in a
	 * feeder.
	 */
	public Equipment AdditionalGroupedEquipment;

	public EquipmentContainer(){

	}
}//end EquipmentContainer