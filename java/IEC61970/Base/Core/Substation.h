///////////////////////////////////////////////////////////
//  Substation.h
//  Implementation of the Class Substation
//  Created on:      25-Dec-2023 8:32:03 PM
///////////////////////////////////////////////////////////

#if !defined(EA_9BF0E119_6F6F_4742_81E3_6711D0A74645__INCLUDED_)
#define EA_9BF0E119_6F6F_4742_81E3_6711D0A74645__INCLUDED_

#include "EquipmentContainer.h"
#include "VoltageLevel.h"
#include "Bay.py"
#include "java\IEC61970\IEC61970\Base\DC\DCConverterUnit.java"
#include "Feeder.h"

/**
 * A collection of equipment for purposes other than generation or utilization,
 * through which electric energy in bulk is passed for the purposes of switching
 * or modifying its characteristics. 
 */
class Substation : public EquipmentContainer
{

public:
	Substation();
	/**
	 * The voltage levels within this substation.
	 */
	VoltageLevel *VoltageLevels;
	/**
	 * Bays contained in the substation.
	 */
	Bay *Bays;
	/**
	 * The DC converter unit belonging of the substation.
	 */
	DCConverterUnit *DCConverterUnit;
	/**
	 * The normal energized feeders of the substation. Also used for naming purposes.
	 */
	Feeder *NormalEnergizedFeeder;

};
#endif // !defined(EA_9BF0E119_6F6F_4742_81E3_6711D0A74645__INCLUDED_)
