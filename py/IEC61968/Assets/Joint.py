from IEC61968.Assets.Asset import Asset
from IEC61968.InfIEC61968.InfAssets.JointConfigurationKind import JointConfigurationKind
from IEC61968.InfIEC61968.InfAssets.JointFillKind import JointFillKind


class Joint(Asset):
    """
    Joint connects two or more cables. It includes the portion of cable under wipes,
    welds, or other seals.
    @created 29-Dec-2023 5:27:44 PM
    """
    def __init__(self):
        super().__init__()
        self.configuration_kind = JointConfigurationKind.WIRES1TO1  # Configuration of joint
        self.fill_kind = JointFillKind.AIR_NO_FILLING  # Material used to fill the joint
        self.insulation = ""  # The type of insulation around the joint