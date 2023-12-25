from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Location import Location
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint


class UsagePointLocation(Location):
    def __init__(self):
        super().__init__()
        self.access_method = ""  # Method for the service person to access this usage point location. For example, a description of where to obtain a key if the facility is unmanned and secured.
        self.remark = ""  # Remarks about this location.
        self.site_access_problem = ""  # Problems previously encountered when visiting or performing work at this location. Examples include: bad dog, violent customer, verbally abusive occupant, obstructions, safety hazards, etc.
        self.usage_points = [UsagePoint()]  # All usage points at this location.
