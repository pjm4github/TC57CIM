class AllocationResultValues:
    """
    Models Market clearing results in terms of price and MW values.
    """
    def __init__(self):
        self.aggregate_type = str()  # "1" -- "Detail", "2" -- "Aggregate by Market service type", "3" -- "Aggregate by "AllocationEnergyType"
        self.allocation_mw_hour = 1.0  # Allocation in MW hours
        self.allocation_price = 1.0  # Allocation price
        self.energy_type_code = str()  # Energy type code
        self.market_service_type = str()  # ME, SR, NR, DAC, DEC
