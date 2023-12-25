# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class PanPricingDetail:
    
    def __init__(self):
        self.alternate_cost_delivered = 1.0
        self.alternate_cost_unit = ""
        self.current_time_date = DateTime()
        self.generation_price = Money()
        self.generation_price_ratio = 1.0
        self.price = Money()
        self.price_ratio = 1.0
        self.price_tier = 0
        self.price_tier_count = 0
        self.price_tier_label = ""
        self.rate_label = ""
        self.register_tier = ""
        self.unit_of_measure = ""
