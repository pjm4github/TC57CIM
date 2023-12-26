///////////////////////////////////////////////////////////
//  ServiceLocation.h
//  Implementation of the Class ServiceLocation
//  Created on:      25-Dec-2023 8:45:24 PM
///////////////////////////////////////////////////////////

#if !defined(EA_A9DD3339_A667_4021_86E1_3478BBB383D7__INCLUDED_)
#define EA_A9DD3339_A667_4021_86E1_3478BBB383D7__INCLUDED_

#include "String.h"
#include "Boolean.h"
#include "IEC61968\Metering\EndDevice.java"
#include "UsagePoint.h"
#include "TroubleTicket.h"
#include "WorkLocation.py"

/**
 * A real estate location, commonly referred to as premises.
 */
class ServiceLocation : public WorkLocation
{

public:
	ServiceLocation();
	/**
	 * Method for the service person to access this service location. For example, a
	 * description of where to obtain a key if the facility is unmanned and secured.
	 */
	String accessMethod;
	/**
	 * True if inspection is needed of facilities at this service location. This could
	 * be requested by a customer, due to suspected tampering, environmental concerns
	 * (e.g., a fire in the vicinity), or to correct incompatible data.
	 */
	Boolean needsInspection;
	/**
	 * Problems previously encountered when visiting or performing work on this
	 * location. Examples include: bad dog, violent customer, verbally abusive
	 * occupant, obstructions, safety hazards, etc.
	 */
	String siteAccessProblem;
	/**
	 * All end devices that measure the service delivered to this service location.
	 */
	EndDevice *EndDevices;
	/**
	 * All usage points delivering service (of the same type) to this service location.
	 */
	UsagePoint *UsagePoints;
	TroubleTicket *TroubleTicket;

};
#endif // !defined(EA_A9DD3339_A667_4021_86E1_3478BBB383D7__INCLUDED_)
