from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.Customer import Customer
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.IncidentHazard import IncidentHazard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.TroubleReportingKind import TroubleReportingKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.Incident import Incident
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class TroubleTicket(Document):
    """
    Description of a problem in the field that may be reported in a trouble ticket
    or come from another source. It may have to do with an outage.
    """

    def __init__(self):
        """
        Constructor for TroubleTicket.
        """
        super().__init__()
        self.comment = str()
        """
        Free-form comment associated with the trouble call for example, "customer
        reported a large flash", etc.
        """

        self.date_time_of_report = DateTime()
        """
        Date and time the trouble has been reported.
        """

        self.first_responder_status = str()
        """
        Indicates whether the first responder such as police, fire department etc.has
        been notified and whether they are on site or en route.
        """

        self.multiple_premises = False
        """
        Set to true if the outage report indicated that other neighbors are also out of
        power.
        """

        self.reporting_kind = TroubleReportingKind.IVR
        """
        Indicates how the customer reported trouble.
        """

        self.resolved_date_time = DateTime()
        """
        Date and time this trouble ticket has been resolved.
        """

        self.trouble_code = ""
        """
        Trouble code (e.g., power down, flickering lights, partial power, etc).
        """

        self.incident_hazard = IncidentHazard()
        """
        All hazards reported with this trouble ticket.
        """

        self.customer = Customer()
        """
        Customer for whom this trouble ticket is relevant.
        """

        self.incident = Incident()
        """
        Incident reported in this trouble ticket.
        """
