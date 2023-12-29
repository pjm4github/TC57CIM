# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:12:35 2023
from typing import Union

from IEC61968.Common.Agreement import Agreement


class IntSchedAgreement(Agreement):
    """
    A type of agreement that provides the default method by which interchange
    schedules are to be integrated to obtain hourly MWh schedules for accounting.
    @created 27-Dec-2023 3:10:38 PM
    """

    def __init__(self) -> None:
        super().__init__()

        """
        The default method by which interchange schedules are to be integrated to
        obtain hourly MWh schedules for accounting. Method #1 is to integrate the
        instantaneous schedule between the hourly boundaries. Method #2 compensates
        for any up/down ramping that occurs across the hourly boundary (this is
        called block accounting).
        """
        self.default_integration_method: Union[str, None] = ""
