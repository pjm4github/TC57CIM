# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class DateTimeInterval:
    """
    Interval between two date and time points.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        """
        Start date and time of this interval.
        """
        self.start: DateTime = DateTime()

        """
        End date and time of this interval.
        """
        self.end:  DateTime = DateTime()

