///////////////////////////////////////////////////////////
//  TroubleTicket.h
//  Implementation of the Class TroubleTicket
//  Created on:      25-Dec-2023 8:45:25 PM
//  Original author: T. Kostic
///////////////////////////////////////////////////////////

#if !defined(EA_B8F797BD_D7A0_4e72_9AF0_5BCD956B922C__INCLUDED_)
#define EA_B8F797BD_D7A0_4e72_9AF0_5BCD956B922C__INCLUDED_

#include "String.h"
#include "DateTime.py"
#include "Boolean.h"
#include "IEC61968\Customers\TroubleReportingKind.java"
#include "IEC61968\Customers\IncidentHazard.java"
#include "Customer.h"
#include "Incident.h"
#include "Document.h"

class TroubleTicket : public Document
{

public:
	TroubleTicket();
	/**
	 * Free-form comment associated with the trouble call for example, "customer
	 * reported a large flash", etc.
	 */
	String comment;
	/**
	 * Date and time the trouble has been reported.
	 */
	DateTime dateTimeOfReport;
	/**
	 * Indicates whether the first responder such as police, fire department etc.has
	 * been notified and whether they are on site or en route.
	 */
	String firstResponderStatus;
	/**
	 * Set to true if the outage report indicated that other neighbors are also out of
	 * power.
	 */
	Boolean multiplePremises;
	/**
	 * Indicates how the customer reported trouble.
	 */
	TroubleReportingKind reportingKind;
	/**
	 * Date and time this trouble ticket has been resolved.
	 */
	DateTime resolvedDateTime;
	/**
	 * Trouble code (e.g., power down, flickering lights, partial power, etc).
	 */
	String troubleCode;
	/**
	 * All hazards reported with this trouble ticket.
	 */
	IncidentHazard *IncidentHazard;
	/**
	 * Customer for whom this trouble ticket is relevant.
	 */
	Customer *Customer;
	/**
	 * Incident reported in this trouble ticket
	 */
	Incident *Incident;

};
#endif // !defined(EA_B8F797BD_D7A0_4e72_9AF0_5BCD956B922C__INCLUDED_)
