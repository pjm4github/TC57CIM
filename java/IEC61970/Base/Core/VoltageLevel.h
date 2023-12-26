///////////////////////////////////////////////////////////
//  VoltageLevel.h
//  Implementation of the Class VoltageLevel
//  Created on:      25-Dec-2023 8:32:05 PM
///////////////////////////////////////////////////////////

#if !defined(EA_E8D7CB91_E676_4b7d_B102_96AAB2F60841__INCLUDED_)
#define EA_E8D7CB91_E676_4b7d_B102_96AAB2F60841__INCLUDED_

#include "Voltage.h"
#include "EquipmentContainer.h"
#include "Bay.py"
#include "BaseVoltage.py"

/**
 * A collection of equipment at one common system voltage forming a switchgear.
 * The equipment typically consist of breakers, busbars, instrumentation, control,
 * regulation and protection devices as well as assemblies of all these.
 */
class VoltageLevel : public EquipmentContainer
{

public:
	VoltageLevel();
	/**
	 * The bus bar's high voltage limit
	 */
	Voltage highVoltageLimit;
	/**
	 * The bus bar's low voltage limit
	 */
	Voltage lowVoltageLimit;
	/**
	 * The bays within this voltage level.
	 */
	Bay *Bays;
	/**
	 * The base voltage used for all equipment within the voltage level.
	 */
	BaseVoltage *BaseVoltage;

};
#endif // !defined(EA_E8D7CB91_E676_4b7d_B102_96AAB2F60841__INCLUDED_)
