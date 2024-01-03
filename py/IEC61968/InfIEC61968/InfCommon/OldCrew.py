# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023

from IEC61968.Common.Crew import Crew
from IEC61968.Common.Location import Location
from IEC61968.InfIEC61968.InfLocations.Route import Route
from IEC61968.InfIEC61968.InfWork.Assignment import Assignment
from IEC61968.InfIEC61968.InfWork.ShiftPattern import ShiftPattern


class OldCrew(Crew):
    """A crew is a group of people with specific skills, tools, and vehicles."""

    def __init__(self) -> None:
        super().__init__()
        # Classification by utility's work management standards and practices.
        self.type: str = ""
        self.route: Route = Route()
        # All Assignments for this Crew.
        self.assignments: Assignment = Assignment()
        self.shift_patterns: ShiftPattern = ShiftPattern()
        self.locations: Location = Location()
