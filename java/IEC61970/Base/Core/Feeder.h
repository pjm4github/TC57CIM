///////////////////////////////////////////////////////////
//  Feeder.h
//  Implementation of the Class Feeder
//  Created on:      25-Dec-2023 8:31:58 PM
//  Original author: selaost1
///////////////////////////////////////////////////////////

#if !defined(EA_D70D4A78_CA84_4834_AF4A_2DE784A87684__INCLUDED_)
#define EA_D70D4A78_CA84_4834_AF4A_2DE784A87684__INCLUDED_

#include "EquipmentContainer.h"
#include "Substation.h"
#include "Terminal.h"

/**
 * A collection of equipment for organizational purposes, used for grouping
 * distribution resources.
 * The organization a feeder does not necessarily reflect connectivity or current
 * operation state.
 */
class Feeder : public EquipmentContainer
{

public:
	Feeder();
	/**
	 * The secondary substations that are normally energized from the feeder.  Used
	 * for naming purposes.   Should be consistent with the other associations for
	 * energizing terminal specification and the feeder energization specification.
	 */
	Substation *NamingSecondarySubstation;
	/**
	 * The normal head terminal or terminals of the feeder.
	 */
	Terminal *NormalHeadTerminal;
	/**
	 * The substations that are normally energized by the feeder.
	 */
	Substation *NormalEnergizedSubstation;

};
#endif // !defined(EA_D70D4A78_CA84_4834_AF4A_2DE784A87684__INCLUDED_)
