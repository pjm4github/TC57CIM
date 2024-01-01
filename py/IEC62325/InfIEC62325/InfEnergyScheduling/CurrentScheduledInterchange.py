# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from typing import Optional

from IEC62325.InfIEC62325.InfEnergyScheduling.InternalControlArea import InternalControlArea


class CurrentScheduledInterchange:
    """
    Control area current net tie (scheduled interchange) sent to real time dispatch.
    @created 27-Dec-2023 12:43:40 PM
    """
    
    def __init__(self) -> None:
        """
        Current control area net tie MW (the sum of the tie line flows, i.e the sum of
        flows into and out of the control area), the current instantaneous scheduled
        interchange.
        
        Use Emergency Schedule
        Attribute Usage: Emergency use indicator, false = Emergency Schedular OFF, true
        = Emergency Schedular ON.
        """
        self.current_net_tie_mwOptional[float] = 0.0
        self.use_emergency_scheduleOptional[bool] = False
        self.internal_control_areaOptional[InternalControlArea] = InternalControlArea()
