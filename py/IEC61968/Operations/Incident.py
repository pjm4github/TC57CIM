from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Location import Location
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Operator import Operator
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.CustomerNotification import CustomerNotification
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.IncidentHazard import IncidentHazard
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.Outage import Outage
from CIM_STD_PYTHON.TC57CIM.IEC61968.Work.Work import Work


class Incident(Document):
    """
    Description of a problem in the field that may be reported in a trouble ticket
    or come from another source. It may have to do with an outage.
    """

    def __init__(self):
        """
        Constructor for Incident.
        """
        super().__init__()
        self.cause = ""
        """
        Cause of this incident.
        """

        self.customer_notifications = CustomerNotification()
        """
        All notifications for a customer related to the status change of this incident.
        """

        self.outage = Outage()
        """
        Outage for this incident.
        """

        self.incident_hazard = IncidentHazard()
        """
        All hazards associated with this incident.
        """

        self.works = Work()
        """
        All works addressing this incident.
        """

        self.location = Location()
        """
        Location of this incident.
        """

        self.owner = Operator()
        """
        Operator who owns this incident.
        """
