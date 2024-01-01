from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61970.Base.Domain.ApparentPower import ApparentPower
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.ReactivePower import ReactivePower
from IEC61970.Base.Domain.Voltage import Voltage


class ShuntCompensatorInfo(AssetInfo):
    def __init__(self):
        # Maximum allowed apparent power loss.
        super().__init__()
        self.max_power_loss = ApparentPower()

        # Rated current.
        self.rated_current = CurrentFlow()

        # Rated reactive power.
        self.rated_reactive_power = ReactivePower()

        # Rated voltage.
        self.rated_voltage = Voltage()

        self.shunt_compensator_control = ShuntCompensatorControl()