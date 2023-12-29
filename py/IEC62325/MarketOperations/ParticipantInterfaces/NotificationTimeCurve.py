# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from IEC61970.Base.Core.Curve import Curve


class NotificationTimeCurve(Curve):
    """
    Notification time curve as a function of down-time. Relationship between
    notification time (Y1-axis) and unit startup time (Y2-axis) vs. unit
    elapsed down time (X-axis).
    @created 28-Dec-2023 5:22:44 PM
    """

    def __init__(self) -> None:
        super().__init__()
