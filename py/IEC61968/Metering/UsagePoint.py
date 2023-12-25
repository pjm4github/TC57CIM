from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ConfigurationEvent import ConfigurationEvent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.PhaseCode import PhaseCode
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage


class UsagePoint(IdentifiedObject):
    """
    Logical or physical point in the network to which readings or events may be
    attributed. Used at the place where a physical or virtual meter may be located;
    however, it is not required that a meter be present.
    """

    def __init__(self):
        """
        Constructor for UsagePoint.
        """
        super().__init__()
        self.ami_billing_ready = AmiBillingReadyKind()
        """
        Tracks the lifecycle of the metering installation at a usage point with respect
        to readiness for billing via advanced metering infrastructure reads.
        """

        self.check_billing = True
        """
        True if as a result of an inspection or otherwise, there is a reason to suspect
        that a previous billing may have been performed with erroneous data. Value
        should be reset once this potential discrepancy has been resolved.
        """

        self.connection_state = UsagePointConnectedKind()
        """
        State of the usage point with respect to connection to the network.
        """

        self.estimated_load = CurrentFlow()
        """
        Estimated load.
        """

        self.grounded = True
        """
        True if grounded.
        """

        self.is_sdp = True
        """
        If true, this usage point is a service delivery point, i.e., a usage point
        where the ownership of the service changes hands.
        """

        self.is_virtual = True
        """
        If true, this usage point is virtual, i.e., no physical location exists in the
        network where a meter could be located to collect the meter readings. For
        example, one may define a virtual usage point to serve as an aggregation of
        usage for all of a company's premises distributed widely across the
        distribution territory. Otherwise, the usage point is physical, i.e., there is
        a logical point in the network where a meter could be located to collect meter
        readings.
        """

        self.minimal_usage_expected = True
        """
        If true, minimal or zero usage is expected at this usage point for situations
        such as premises vacancy, logical or physical disconnect. It is used for
        readings validation and estimation.
        """

        self.nominal_service_voltage = Voltage()
        """
        Nominal service voltage.
        """

        self.outage_region = ""
        """
        Outage region in which this usage point is located.
        """

        self.phase_code = PhaseCode()
        """
        Phase code. Number of wires and specific nominal phases can be deduced from
        enumeration literal values. For example, ABCN is three-phase, four-wire, s12n
        (splitSecondary12N) is single-phase, three-wire, and s1n and s2n are single-
        phase, two-wire.
        """

        self.rated_current = CurrentFlow()
        """
        Current flow that this usage point is configured to deliver.
        """

        self.rated_power = ActivePower()
        """
        Active power that this usage point is configured to deliver.
        """

        self.read_cycle = ""
        """
        Cycle day on which the meter for this usage point will normally be read.
        Usually correlated with the billing cycle.
        """

        self.read_route = ""
        """
        Identifier of the route to which this usage point is assigned for purposes of
        meter reading. Typically used to configure hand held meter reading systems
        prior to collection of reads.
        """

        self.service_delivery_remark = ""
        """
        Remarks about this usage point, for example the reason for it being rated with
        a non-nominal priority.
        """

        self.service_priority = ""
        """
        Priority of service for this usage point. Note that usage points at the same
        service location can have different priorities.
        """

        self.service_multipliers = ServiceMultiplier()
        """
        All multipliers applied at this usage point.
        """

        self.end_devices = EndDevice()
        """
        All end devices at this usage point.
        """

        self.equipments = Equipment()
        """
        All equipment connecting this usage point to the electrical grid.
        """

        self.service_category = ServiceCategory()
        """
        Service category delivered by this usage point.
        """

        self.configuration_events = ConfigurationEvent()
        """
        All configuration events created for this usage point.
        """
   