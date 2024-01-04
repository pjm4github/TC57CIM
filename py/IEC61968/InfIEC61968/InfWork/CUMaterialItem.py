# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.CompatibleUnit import CompatibleUnit
from IEC61968.InfIEC61968.InfWork.TypeMaterial import TypeMaterial
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.IntegerQuantity import IntegerQuantity


class CUMaterialItem(WorkIdentifiedObject):
    """
    Compatible unit of a consumable supply item. For example, nuts, bolts, brackets,
    glue, etc.
    @created 29-Dec-2023 9:12:48 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.corporate_code: Optional[str] = str()  # Code for material.
        self.quantity: Optional[IntegerQuantity] = IntegerQuantity()  # Quantity of the TypeMaterial for this CU, used to determine estimated costs based on a per unit cost or a cost per unit length specified in the TypeMaterial.
        self.status: Optional[Status] = Status()
        self.type_material: Optional[TypeMaterial] = TypeMaterial()
        self.compatible_units: Optional[CompatibleUnit] = CompatibleUnit()

