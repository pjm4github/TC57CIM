# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.CUMaterialItem import CUMaterialItem
from IEC61968.InfIEC61968.InfWork.CompatibleUnit import CompatibleUnit
from IEC61968.InfIEC61968.InfWork.WorkActionKind import WorkActionKind
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class PropertyUnit(WorkIdentifiedObject):
    """
    Unit of property for reporting purposes.
    @created 29-Dec-2023 9:17:51 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.accounting_usage: Optional[str] = str()  # A code1 that identifies appropriate type of property accounts such as distribution, streetlgihts, communications.
        self.activity_code: Optional[WorkActionKind] = WorkActionKind.REMOVE  # Activity code1 identifies a specific and distinguishable work action.
        self.property_account: Optional[str] = str()  # Used for property record accounting. For example, in the USA, this would be a FERC account.
        self.status: Optional[Status] = Status()
        self.cum_material_items: Optional[CUMaterialItem] = CUMaterialItem()
        self.compatible_units: Optional[CompatibleUnit] = CompatibleUnit()
