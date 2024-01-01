# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 16:42:20 2023
from datetime import datetime
from typing import Any

from IEC61968.InfIEC61968.InfCommon.Craft import Craft
from IEC61968.InfIEC61968.InfCommon.SkillLevelKind import SkillLevelKind
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval



class Skill:
    """
    Proficiency level of a craft, which is required to operate or maintain a
    particular type of asset and/or perform certain types of work.
    @created 29-Dec-2023 6:03:20 PM
    """
    
    def __init__(self) -> None:
        self.certification_period: DateTimeInterval = DateTimeInterval()  # Interval between the certification and its expiry
        self.effective_date_time: DateTime = DateTime()  # Date and time the skill became effective
        self.level: SkillLevelKind  = SkillLevelKind() # Level of skill for a Craft
        self.crafts: Craft = Craft()
        self.qualification_requirements: QualificationRequirement = QualificationRequirement()
