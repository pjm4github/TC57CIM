# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
# Relationship between reservoir volume and reservoir level. The volume is at the y-axis and the reservoir level at the x-axis.
# @created 02-Jan-2024 10:56:45 PM
from IEC61970.Base.Core.Curve import Curve


class LevelVsVolumeCurve(Curve):
    """
    Relationship between reservoir volume and reservoir level.
    The volume is at the y-axis and the reservoir level at the x-axis.
    """

    def __init__(self):
        super().__init__()
