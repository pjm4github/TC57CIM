# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.CompatibleUnit import CompatibleUnit
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61968.Work.WorkAsset import WorkAsset
from IEC61970.Base.Domain.CostRate import CostRate


class CUWorkEquipmentItem(WorkIdentifiedObject):
    """
    Compatible unit for various types of WorkEquipmentAssets, including vehicles.
    @created 29-Dec-2023 9:12:59 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.equip_code: Optional[str] = str()  # The equipment type code1.
        self.rate: Optional[CostRate] = CostRate()  # Standard usage rate for the type of vehicle.
        self.status: Optional[Status] = Status()
        self.compatible_units: Optional[CompatibleUnit] = CompatibleUnit()
        self.type_asset: Optional[WorkAsset] = WorkAsset()
