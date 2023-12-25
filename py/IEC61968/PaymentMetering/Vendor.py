# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.VendorShift import VendorShift
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Vendor(IdentifiedObject):

    def __init__(self):
        super().__init__()
        # 	 * All vendor shifts opened and owned by this vendor.
        self.vendor_shifts = [VendorShift()]
