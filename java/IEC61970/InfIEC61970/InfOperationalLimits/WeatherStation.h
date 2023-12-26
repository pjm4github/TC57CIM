///////////////////////////////////////////////////////////
//  WeatherStation.h
//  Implementation of the Class WeatherStation
//  Created on:      25-Dec-2023 8:32:05 PM
//  Original author: akamath
///////////////////////////////////////////////////////////

#if !defined(EA_E72504CB_D878_4df0_97B8_7B272BB11AFF__INCLUDED_)
#define EA_E72504CB_D878_4df0_97B8_7B272BB11AFF__INCLUDED_

#include "PowerSystemResource.py"

/**
 * This represents a source of ambient temperature.
 */
class WeatherStation : public PowerSystemResource
{

public:
	WeatherStation();

};
#endif // !defined(EA_E72504CB_D878_4df0_97B8_7B272BB11AFF__INCLUDED_)
