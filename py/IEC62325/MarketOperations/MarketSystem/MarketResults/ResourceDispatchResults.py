# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime


class ResourceDispatchResults:
    """
    The ResourceDispatchResults class provides market results that can be provided
    to a SC. The specific data provided consists of several indicators such as
    contingency flags, blocked start up, and RMR dispatch. It also provides the
    projected overall and the regulating status of the resource.
    @created 28-Dec-2023 8:25:53 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ResourceDispatchResults
        """
        self.blocked_dispatch: str = ""  # Blocked Dispatch Indicator (Yes/No)
        self.blocked_publish_dop: str = ""  # Block sending DOP to ADS (Y/N)
        self.contingency_flag: str = ""  # Contingent Operating Reserve Indicator (Yes/No)
        self.limit_indicator: str = ""  # Indicate which limit is the constraints
        self.lower_limit: float = 0.0  # Resource energy ramping lower limit
        self.max_ramp_rate: float = 0.0  # Maximum ramp rate
        self.operating_limit_high: float = 0.0  # The upper operating limit incorporating any derate used by the RTD for the Binding Interval
        self.operating_limit_low: float = 0.0  # The lower operating limit incorporating any derate used by the RTD for the Binding Interval
        self.penalty_dispatch_indicator: str = ""  # Penalty Dispatch Indicator (Yes / No) indicating an un-economic adjustment
        self.regulating_limit_high: float = 0.0  # The upper regulating limit incorporating any derate used by the RTD for the Binding Interval
        self.regulating_limit_low: float = 0.0  # The lower regulating limit incorporating any derate used by the RTD for the Binding Interval
        self.resource_status: str = ""  # Unit Commitment Status (On/Off/Starting)
        self.total_schedule: float = 0.0  # Resource total upward schedule. total schedule = En + all AS per resource per interval
        self.update_timestamp: DateTime = DateTime()
        self.update_type: str = ""
        self.update_user: str = ""
        self.upper_limit: float = 0.0  # Resource energy ramping upper limit
