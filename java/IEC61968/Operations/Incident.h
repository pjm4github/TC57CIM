///////////////////////////////////////////////////////////
//  Incident.h
//  Implementation of the Class Incident
//  Created on:      25-Dec-2023 8:45:22 PM
//  Original author: Margaret
///////////////////////////////////////////////////////////

#if !defined(EA_F9303DC5_AC62_4661_A71D_D728A66F56F1__INCLUDED_)
#define EA_F9303DC5_AC62_4661_A71D_D728A66F56F1__INCLUDED_

#include "String.h"
#include "CustomerNotification.h"
#include "IEC61968\Operations\Outage.java"
#include "IEC61968\Customers\IncidentHazard.java"
#include "Work.py"
#include "Document.h"
#include "IEC61968\Common\Location.java"
#include "IEC61968\Common\Operator.java"

/**
 * Description of a problem in the field that may be reported in a trouble ticket
 * or come from another source. It may have to do with an outage.
 */
class Incident : public Document
{

public:
	Incident();
	/**
	 * Cause of this incident.
	 */
	String cause;
	/**
	 * All notifications for a customer related to the status change of this incident.
	 */
	CustomerNotification *CustomerNotifications;
	/**
	 * Outage for this incident.
	 */
	Outage *Outage;
	/**
	 * All hazards associated with this incident.
	 */
	IncidentHazard *IncidentHazard;
	/**
	 * All works addressing this incident.
	 */
	Work *Works;
	/**
	 * Location of this incident.
	 */
	Location *Location;
	/**
	 * Operator who owns this incident.
	 */
	Operator *Owner;

};
#endif // !defined(EA_F9303DC5_AC62_4661_A71D_D728A66F56F1__INCLUDED_)
