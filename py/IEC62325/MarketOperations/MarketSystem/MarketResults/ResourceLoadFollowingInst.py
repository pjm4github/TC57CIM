# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from datetime import datetime

from IEC61970.Base.Domain.DateTime import DateTime


class ResourceLoadFollowingInst:
    """
    Model of market clearing results for resources that bid to follow load.
    @created 28-Dec-2023 8:26:04 PM
    """

    def __init__(self) -> None:
        self.calc_load_following_MW: float = 0.0
        """weighted average for RTPD and RTCD and same for RTID"""
        self.disp_window_high_limit: float = 0.0
        self.disp_window_low_limit: float = 0.0
        """
        Unique instruction id per instruction, assigned by the SC and provided to ADS.
        ADS passes through.
        """
        self.instruction_id: str = ""
        """
        The start of the time interval for which requirement is defined.
        """
        self.interval_start_time: DateTime = DateTime()
