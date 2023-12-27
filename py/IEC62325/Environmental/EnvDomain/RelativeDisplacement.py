# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.Displacement import Displacement
from IEC62325.Environmental.EnvDomain.RelativeDisplacementKind import RelativeDisplacementKind


class RelativeDisplacement:
    """
    Vertical displacement relative to either sealevel, ground or the center of the earth.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        self.displacement = Displacement()
        self.kind = RelativeDisplacementKind.GROUND
