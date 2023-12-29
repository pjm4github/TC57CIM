# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC62325.MarketOperations.MktDomain.SelfScpyeduleBreakdownType import SelfScheduleBreakdownType


class SelfScheduleBreakdown:
    """
    Model of Self Schedules Results. Includes self schedule MW, and type of self
    schedule for each self schedule type included in total self schedule MW value
    found in ResourceAwardInstruction.
    """
    
    def __init__(self) -> None:
        self.self_sched_mw: float = 0.0
        self.self_sched_type: SelfScheduleBreakdownType = SelfScheduleBreakdownType.ETC
