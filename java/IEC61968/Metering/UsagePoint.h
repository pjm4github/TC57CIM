///////////////////////////////////////////////////////////
//  UsagePoint.h
//  Implementation of the Class UsagePoint
//  Created on:      25-Dec-2023 8:45:25 PM
///////////////////////////////////////////////////////////

#if !defined(EA_54305061_534D_4932_AAB2_8E3648E1570A__INCLUDED_)
#define EA_54305061_534D_4932_AAB2_8E3648E1570A__INCLUDED_

#include "IEC61968\Metering\AmiBillingReadyKind.java"
#include "Boolean.h"
#include "IEC61968\Metering\UsagePointConnectedKind.java"
#include "CurrentFlow.h"
#include "Voltage.h"
#include "String.h"
#include "PhaseCode.py"
#include "ActivePower.h"
#include "IEC61968\Metering\ServiceMultiplier.java"
#include "IEC61968\Metering\EndDevice.java"
#include "Equipment.py"
#include "IdentifiedObject.py"
#include "ServiceCategory.h"
#include "ConfigurationEvent.py"

/**
 * Logical or physical point in the network to which readings or events may be
 * attributed. Used at the place where a physical or virtual meter may be located;
 * however, it is not required that a meter be present.
 */
class UsagePoint : public IdentifiedObject
{

public:
	UsagePoint();
	/**
	 * Tracks the lifecycle of the metering installation at a usage point with respect
	 * to readiness for billing via advanced metering infrastructure reads.
	 */
	AmiBillingReadyKind amiBillingReady;
	/**
	 * True if as a result of an inspection or otherwise, there is a reason to suspect
	 * that a previous billing may have been performed with erroneous data. Value
	 * should be reset once this potential discrepancy has been resolved.
	 */
	Boolean checkBilling;
	/**
	 * State of the usage point with respect to connection to the network.
	 */
	UsagePointConnectedKind connectionState;
	/**
	 * Estimated load.
	 */
	CurrentFlow estimatedLoad;
	/**
	 * True if grounded.
	 */
	Boolean grounded;
	/**
	 * If true, this usage point is a service delivery point, i.e., a usage point
	 * where the ownership of the service changes hands.
	 */
	Boolean isSdp;
	/**
	 * If true, this usage point is virtual, i.e., no physical location exists in the
	 * network where a meter could be located to collect the meter readings. For
	 * example, one may define a virtual usage point to serve as an aggregation of
	 * usage for all of a company's premises distributed widely across the
	 * distribution territory. Otherwise, the usage point is physical, i.e., there is
	 * a logical point in the network where a meter could be located to collect meter
	 * readings.
	 */
	Boolean isVirtual;
	/**
	 * If true, minimal or zero usage is expected at this usage point for situations
	 * such as premises vacancy, logical or physical disconnect. It is used for
	 * readings validation and estimation.
	 */
	Boolean minimalUsageExpected;
	/**
	 * Nominal service voltage.
	 */
	Voltage nominalServiceVoltage;
	/**
	 * Outage region in which this usage point is located.
	 */
	String outageRegion;
	/**
	 * Phase code. Number of wires and specific nominal phases can be deduced from
	 * enumeration literal values. For example, ABCN is three-phase, four-wire, s12n
	 * (splitSecondary12N) is single-phase, three-wire, and s1n and s2n are single-
	 * phase, two-wire.
	 */
	PhaseCode phaseCode;
	/**
	 * Current flow that this usage point is configured to deliver.
	 */
	CurrentFlow ratedCurrent;
	/**
	 * Active power that this usage point is configured to deliver.
	 */
	ActivePower ratedPower;
	/**
	 * Cycle day on which the meter for this usage point will normally be read.
	 * Usually correlated with the billing cycle.
	 */
	String readCycle;
	/**
	 * Identifier of the route to which this usage point is assigned for purposes of
	 * meter reading. Typically used to configure hand held meter reading systems
	 * prior to collection of reads.
	 */
	String readRoute;
	/**
	 * Remarks about this usage point, for example the reason for it being rated with
	 * a non-nominal priority.
	 */
	String serviceDeliveryRemark;
	/**
	 * Priority of service for this usage point. Note that usage points at the same
	 * service location can have different priorities.
	 */
	String servicePriority;
	/**
	 * All multipliers applied at this usage point.
	 */
	ServiceMultiplier *ServiceMultipliers;
	/**
	 * All end devices at this usage point.
	 */
	EndDevice *EndDevices;
	/**
	 * All equipment connecting this usage point to the electrical grid.
	 */
	Equipment *Equipments;
	/**
	 * Service category delivered by this usage point.
	 */
	ServiceCategory *ServiceCategory;
	/**
	 * All configuration events created for this usage point.
	 */
	ConfigurationEvent *ConfigurationEvents;

};
#endif // !defined(EA_54305061_534D_4932_AAB2_8E3648E1570A__INCLUDED_)
