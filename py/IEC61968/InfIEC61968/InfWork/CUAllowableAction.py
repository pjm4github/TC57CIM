# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.CompatibleUnit import CompatibleUnit
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class CUAllowableAction(WorkIdentifiedObject):
    """
    Allowed actions: Install, Remove, Transfer, Abandon, etc.
    @created 29-Dec-2023 9:11:29 PM
    """

    def __init__(self) -> None:
        super().__init__()

        self.status: Status = Status()
        self.compatible_units: CompatibleUnit = CompatibleUnit()
