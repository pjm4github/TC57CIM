package IEC61968.Metering;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.String;
import IEC61970.Base.Core.PhaseCode;
import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.Core.Equipment;
import IEC61970.Base.Core.IdentifiedObject;
import IEC61968.Customers.ServiceCategory;
import IEC61968.Common.ConfigurationEvent;

/**
 * Logical or physical point in the network to which readings or events may be
 * attributed. Used at the place where a physical or virtual meter may be located;
 * however, it is not required that a meter be present.
 * @created 03-Jan-2024 1:12:58 PM
 */
public class UsagePoint extends IdentifiedObject {

	/**
	 * Tracks the lifecycle of the metering installation at a usage point with respect
	 * to readiness for billing via advanced metering infrastructure reads.
	 */
	public AmiBillingReadyKind amiBillingReady;
	/**
	 * True if as a result of an inspection or otherwise, there is a reason to suspect
	 * that a previous billing may have been performed with erroneous data. Value
	 * should be reset once this potential discrepancy has been resolved.
	 */
	public Boolean checkBilling;
	/**
	 * State of the usage point with respect to connection to the network.
	 */
	public UsagePointConnectedKind connectionState;
	/**
	 * Estimated load.
	 */
	public CurrentFlow estimatedLoad;
	/**
	 * True if grounded.
	 */
	public Boolean grounded;
	/**
	 * If true, this usage point is a service delivery point, i.e., a usage point
	 * where the ownership of the service changes hands.
	 */
	public Boolean isSdp;
	/**
	 * If true, this usage point is virtual, i.e., no physical location exists in the
	 * network where a meter could be located to collect the meter readings. For
	 * example, one may define a virtual usage point to serve as an aggregation of
	 * usage for all of a company's premises distributed widely across the
	 * distribution territory. Otherwise, the usage point is physical, i.e., there is
	 * a logical point in the network where a meter could be located to collect meter
	 * readings.
	 */
	public Boolean isVirtual;
	/**
	 * If true, minimal or zero usage is expected at this usage point for situations
	 * such as premises vacancy, logical or physical disconnect. It is used for
	 * readings validation and estimation.
	 */
	public Boolean minimalUsageExpected;
	/**
	 * Nominal service voltage.
	 */
	public Voltage nominalServiceVoltage;
	/**
	 * Outage region in which this usage point is located.
	 */
	public String outageRegion;
	/**
	 * Phase code. Number of wires and specific nominal phases can be deduced from
	 * enumeration literal values. For example, ABCN is three-phase, four-wire, s12n
	 * (splitSecondary12N) is single-phase, three-wire, and s1n and s2n are single-
	 * phase, two-wire.
	 */
	public PhaseCode phaseCode;
	/**
	 * Current flow that this usage point is configured to deliver.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Active power that this usage point is configured to deliver.
	 */
	public ActivePower ratedPower;
	/**
	 * Cycle day on which the meter for this usage point will normally be read.
	 * Usually correlated with the billing cycle.
	 */
	public String readCycle;
	/**
	 * Identifier of the route to which this usage point is assigned for purposes of
	 * meter reading. Typically used to configure hand held meter reading systems
	 * prior to collection of reads.
	 */
	public String readRoute;
	/**
	 * Remarks about this usage point, for example the reason for it being rated with
	 * a non-nominal priority.
	 */
	public String serviceDeliveryRemark;
	/**
	 * Priority of service for this usage point. Note that usage points at the same
	 * service location can have different priorities.
	 */
	public String servicePriority;
	/**
	 * All multipliers applied at this usage point.
	 */
	public ServiceMultiplier ServiceMultipliers;
	/**
	 * All end devices at this usage point.
	 */
	public EndDevice EndDevices;
	/**
	 * All equipment connecting this usage point to the electrical grid.
	 */
	public Equipment Equipments;
	/**
	 * Service category delivered by this usage point.
	 */
	public ServiceCategory ServiceCategory;
	/**
	 * All configuration events created for this usage point.
	 */
	public ConfigurationEvent ConfigurationEvents;

	public UsagePoint(){

	}
}//end UsagePoint