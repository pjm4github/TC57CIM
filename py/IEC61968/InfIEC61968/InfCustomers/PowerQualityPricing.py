# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.CostPerEnergyUnit import CostPerEnergyUnit
from IEC61970.Base.Domain.Voltage import Voltage


class PowerQualityPricing(Document):
    """
    Pricing can be based on power quality.
    @created 29-Dec-2023 9:25:37 PM
    """

    def __init__(self) -> None:
        """Constructor for PowerQualityPricing"""
        super().__init__()
        self.emergency_high_volt_limit = Voltage()  # Emergency high voltage limit.
        self.emergency_low_volt_limit = Voltage()  # Emergency low voltage limit.
        self.normal_high_volt_limit = Voltage()  # Normal high voltage limit.
        self.normal_low_volt_limit = Voltage()  # Normal low voltage limit.
        self.power_factor_min: float = 1.0  # Threshold minimum power factor for this PricingStructure.
        # specified in instances where a special charge is levied
        # if the actual power factor for a Service falls below
        # the value specified here.
        self.value_uninterrupted_service_energy = CostPerEnergyUnit()  # Value of uninterrupted service (Cost per
        # energy).
        self.value_uninterrupted_service_p = 1.0  # Value of uninterrupted service (Cost per active power).
        self.volt_imbalance_viol_cost = 1.0  # Voltage imbalance violation cost (Cost per unit Voltage).
        self.volt_limit_viol_cost = 1.0  # Voltage limit violation cost (Cost per unit Voltage).
