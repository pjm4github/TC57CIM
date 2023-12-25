# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.EndDeviceAction import EndDeviceAction
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.PanPricingDetail import PanPricingDetail


class PanPricing(EndDeviceAction):

    def __init__(self):
        super().__init__()
        self.provider_id = 0
        self.pan_pricing_details = PanPricingDetail()
