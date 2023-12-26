///////////////////////////////////////////////////////////
//  MeasurementValueQuality.h
//  Implementation of the Class MeasurementValueQuality
//  Created on:      25-Dec-2023 8:32:00 PM
///////////////////////////////////////////////////////////

#if !defined(EA_0B44AB7E_026E_405b_9C74_E3848F1D0E26__INCLUDED_)
#define EA_0B44AB7E_026E_405b_9C74_E3848F1D0E26__INCLUDED_

#include "Quality61850.h"
#include "MeasurementValueQualityExt.py"

/**
 * Measurement quality flags. Bits 0-10 are defined for substation automation in
 * draft IEC 61850 part 7-3. Bits 11-15 are reserved for future expansion by that
 * document. Bits 16-31 are reserved for EMS applications.
 */
class MeasurementValueQuality : public Quality61850, public MeasurementValueQualityExt
{

public:
	MeasurementValueQuality();

};
#endif // !defined(EA_0B44AB7E_026E_405b_9C74_E3848F1D0E26__INCLUDED_)
