from IEC62325.MarketOperations.MktDomain.ResourceCapacityType import ResourceCapacityType  # Importing ResourceCapacityType class from IEC62325.MarketOperations.MktDomain module
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol  # Importing UnitSymbol class from IEC61970.Base.Domain module

class ResourceCapacity:
    """
    This class models the various capacities of a resource. A resource may have
    numbers of capacities related to operating, ancillary services, energy trade
    and so forth. Capacities may be defined for active power or reactive power.
    @created 28-Dec-2023 8:05:28 PM
    """
    def __init__(self):
        self.capacity_type = ResourceCapacityType.RMR  # Creating an instance of ResourceCapacityType class and assigning it to the 'capacityType' attribute
        self.default_capacity = 0  # Creating an instance of Decimal class and assigning it to the 'defaultCapacity' attribute
        self.maximum_capacity = 0  # Creating an instance of Decimal class and assigning it to the 'maximumCapacity' attribute
        self.minimum_capacity = 0  # Creating an instance of Decimal class and assigning it to the 'minimumCapacity' attribute
        self.unit_symbol = UnitSymbol()  # Creating an instance of UnitSymbol class and assigning it to the 'unitSymbol' attribute

