# ServiceLocation.py
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.TroubleTicket import TroubleTicket
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint


class ServiceLocation(WorkLocation):
    def __init__(self):
        self.accessMethod = ""
        # Method for the service person to access this service location. For example, a
        # description of where to obtain a key if the facility is unmanned and secured.
        self.needsInspection = True
        # True if inspection is needed of facilities at this service location. This could
        # be requested by a customer, due to suspected tampering, environmental concerns
        # (e.g., a fire in the vicinity), or to correct incompatible data.
        self.siteAccessProblem = ""
        # Problems previously encountered when visiting or performing work on this
        # location. Examples include: bad dog, violent customer, verbally abusive
        # occupant, obstructions, safety hazards, etc.
        self.EndDevices = EndDevice()
        # All end devices that measure the service delivered to this service location.
        self.UsagePoints = UsagePoint()
        # All usage points delivering service (of the same type) to this service location.
        self.TroubleTicket = TroubleTicket()
