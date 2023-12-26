///////////////////////////////////////////////////////////
//  EquipmentContainer.h
//  Implementation of the Class EquipmentContainer
//  Created on:      25-Dec-2023 8:31:56 PM
///////////////////////////////////////////////////////////

#if !defined(EA_325E0FF6_53FD_45dd_B8DB_BF7E8F80557A__INCLUDED_)
#define EA_325E0FF6_53FD_45dd_B8DB_BF7E8F80557A__INCLUDED_

#include "Equipment.py"
#include "ConnectivityNodeContainer.py"

/**
 * A modeling construct to provide a root class for containing equipment. 
 */
class EquipmentContainer : public ConnectivityNodeContainer
{

public:
	EquipmentContainer();
	/**
	 * Contained equipment.
	 */
	Equipment *Equipments;
	/**
	 * The additonal contained equipment.  The equipment belong to the equipment
	 * container. The equipment is contained in another equipment container, but also
	 * grouped with this equipment container.  Examples include when a switch
	 * contained in a substation is also desired to be grouped with a line contianer
	 * or when a switch is included in a secondary substation and also grouped in a
	 * feeder.
	 */
	Equipment *AdditionalGroupedEquipment;

};
#endif // !defined(EA_325E0FF6_53FD_45dd_B8DB_BF7E8F80557A__INCLUDED_)
