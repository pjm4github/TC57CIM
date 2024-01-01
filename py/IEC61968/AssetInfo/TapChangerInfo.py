
from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61970.Base.Domain.AngleDegrees import AngleDegrees
from IEC61970.Base.Domain.ApparentPower import ApparentPower
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Voltage import Voltage


class TapChangerInfo(AssetInfo):
    def __init__(self):
        # Basic Insulation Level (BIL) expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond.
        # This is a measure of the ability of the insulation to withstand very high voltage surges.
        super().__init__()
        self.bil = Voltage()

        # Built-in current transformer primary rating.
        self.ct_rating = CurrentFlow()

        # Built-in current transducer ratio.
        self.ct_ratio = 0.0

        # Frequency at which the ratings apply.
        self.frequency = Frequency()

        # Highest possible tap step position, advance from neutral.
        self.high_step = 0

        # Whether this tap changer has under load tap changing capabilities.
        self.is_tcul = False

        # Lowest possible tap step position, retard from neutral.
        self.low_step = 0

        # The neutral tap step position for the winding.
        self.neutral_step = 0

        # Voltage at which the winding operates at the neutral tap setting.
        self.neutral_u = Voltage()

        # Built-in voltage transducer ratio.
        self.pt_ratio = 0.0

        # Rated apparent power.
        self.rated_apparent_power = ApparentPower()

        # Rated current.
        self.rated_current = CurrentFlow()

        # Rated voltage.
        self.rated_voltage = Voltage()

        # Phase shift per step position.
        self.step_phase_increment = AngleDegrees()

        # Tap step increment, in per cent of rated voltage, per step position.
        self.step_voltage_increment = PerCent()