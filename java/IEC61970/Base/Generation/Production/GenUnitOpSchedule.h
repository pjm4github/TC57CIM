///////////////////////////////////////////////////////////
//  GenUnitOpSchedule.h
//  Implementation of the Class GenUnitOpSchedule
//  Created on:      25-Dec-2023 8:31:58 PM
///////////////////////////////////////////////////////////

#if !defined(EA_47340173_25B3_4ed5_8135_C28CD30583EE__INCLUDED_)
#define EA_47340173_25B3_4ed5_8135_C28CD30583EE__INCLUDED_

#include "RegularIntervalSchedule.py"

/**
 * The generating unit's Operator-approved current operating schedule (or plan),
 * typically produced with the aid of unit commitment type analyses. The X-axis
 * represents absolute time. The Y1-axis represents the status (0=off-line and
 * unavailable: 1=available: 2=must run: 3=must run at fixed power value: etc.).
 * The Y2-axis represents the must run fixed power value where required.
 */
class GenUnitOpSchedule : public RegularIntervalSchedule
{

public:
	GenUnitOpSchedule();

};
#endif // !defined(EA_47340173_25B3_4ed5_8135_C28CD30583EE__INCLUDED_)
