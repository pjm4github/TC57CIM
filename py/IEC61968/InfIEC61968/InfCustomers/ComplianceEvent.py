# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from IEC61968.Common.ActivityRecord import ActivityRecord
from IEC61970.Base.Domain.DateTime import DateTime


class ComplianceEvent(ActivityRecord):
    """
    Compliance events are used for reporting regulatory or contract compliance
    issues and/or variances. These might be created as a consequence of local
    business processes and associated rules. It is anticipated that this class will
    be customised extensively to meet local implementation needs.
    Use inherited 'type' to indicate that, for example, expected performance will
    not be met or reported as mandated.
    @created 29-Dec-2023 9:25:00 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.deadline: DateTime = DateTime()  # The deadline for compliance
