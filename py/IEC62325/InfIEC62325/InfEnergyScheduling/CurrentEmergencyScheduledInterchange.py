# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.InfIEC62325.InfEnergyScheduling.InternalControlArea import InternalControlArea


class CurrentEmergencyScheduledInterchange:
    """
    Control area emergency schedules
    @created 27-Dec-2023 12:43:25 PM
    """

    def __init__(self):
        """
        Net tie MW. These are three entries, the current emergency schedule interchange and the two future schedules if they exist.
        """
        self.emergency_schedule_mw: float = 0.0

        """
        Ramp time, the ramping time for a schedule. This is calculated as the remaining time to ramp if a schedule is ramping. 
        Measured in seconds, but can be negative.
        """
        self.emergency_schedule_ramp_time: int = 0

        """
        Net tie time, the start time for a schedule. This is calculated as the current time if a schedule is ramping.
        """
        self.emergency_schedule_start_time: DateTime = DateTime()

        self.internal_control_area: InternalControlArea = InternalControlArea()
