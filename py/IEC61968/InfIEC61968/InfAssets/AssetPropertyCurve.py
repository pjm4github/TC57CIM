# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61970.Base.Core.Curve import Curve


class AssetPropertyCurve(Curve):
    """
    An Asset Property that is described through curves rather than as a data point.
    The relationship is to be defined between an independent variable (X-axis) and
    one or two dependent variables (Y1-axis and Y2-axis).
    @created 29-Dec-2023 6:11:20 PM
    """
    def __init__(self) -> None:
        super().__init__()
