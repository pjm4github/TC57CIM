# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.RealEnergy import RealEnergy
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Currency import Currency
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier


class AccountingUnit:
    """
    Unit for accounting; use either 'energy_unit' or 'currency_unit' to specify the unit for 'value'.
    @created 20-Dec-2023 5:05:00 PM
    """

    def __init__(self):
        """
        Unit of service.
        """
        self.energy_unit = RealEnergy()

        """
        Unit of currency.
        """
        self.monetary_unit = Currency()

        """
        Multiplier for the 'energy_unit' or 'monetary_unit'.
        """
        self.multiplier = UnitMultiplier()

        """
        Value expressed in applicable units.
        """
        self.value = 0.0
