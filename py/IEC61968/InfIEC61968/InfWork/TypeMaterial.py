# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfERPSupport.ErpReqLineItem import ErpReqLineItem
from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61968.Work.MaterialItem import MaterialItem
from IEC61970.Base.Domain.Money import Money


class TypeMaterial(WorkDocument):
    """
    Documentation for a generic material item that may be used for design, work and
    other purposes. Any number of MaterialItems manufactured by various vendors may
    be used to perform this TypeMaterial.
    Note that class analagous to "AssetModel" is not used for material items. This
    is because in some cases, for example, a utility sets up a Master material
    record for a 3 inch long half inch diameter steel bolt and they do not
    necessarily care what specific supplier is providing the material item. As
    different vendors are used to supply the part, the Stock Code of the material
    item can stay the same. In other cases, each time the vendor changes, a new
    stock code1 is set up so they can track material used by vendor. Therefore a
    Material Item "Model" is not typically needed.
    @created 29-Dec-2023 9:19:02 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.cost_type: Optional[str] = ""  # The type of cost to which this Material Item belongs.
        self.est_unit_cost: Optional[Money] = Money()  # The estimated unit cost of this type of material, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it.
        self.quantity: Optional[str] = ""  # The value, unit of measure, and multiplier for the quantity.
        self.stock_item: Optional[bool] = True  # True if item is a stock item (default).
        self.erp_req_line_items: Optional[ErpReqLineItem] = ErpReqLineItem()
        self.material_items: Optional[MaterialItem] = MaterialItem()
