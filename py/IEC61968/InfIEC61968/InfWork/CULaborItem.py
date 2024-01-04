# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.CULaborCode import CULaborCode
from IEC61968.InfIEC61968.InfWork.CompatibleUnit import CompatibleUnit
from IEC61968.InfIEC61968.InfWork.QualificationRequirement import QualificationRequirement
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.CostRate import CostRate
from IEC61970.Base.Domain.Hours import Hours


class CULaborItem(WorkIdentifiedObject):
    """
    Compatible unit labor item.
    @created 29-Dec-2023 9:12:35 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.activity_code: Optional[str] = str()  # Activity code identifies a specific and distinguishable unit of work.
        self.labor_duration: Optional[Hours] = Hours()  # Estimated time to perform work.
        self.labor_rate: Optional[CostRate] = CostRate()  # The labor rate applied for work.
        self.status: Optional[Status] = Status()
        self.qualification_requirements: Optional[QualificationRequirement] = QualificationRequirement()
        self.cu_labor_code: Optional[CULaborCode] = CULaborCode()
        self.compatible_units: Optional[CompatibleUnit] = CompatibleUnit()