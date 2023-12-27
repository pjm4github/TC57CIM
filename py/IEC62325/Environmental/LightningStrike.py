# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.Length import Length
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC62325.Environmental.EnvDomain.Bearing import Bearing
from IEC62325.Environmental.GeosphericPhenomenon import GeosphericPhenomenon



class LightningStrike(GeosphericPhenomenon):
    """
    A cloud-to-ground lightning strike at a particular location.
    @author mcmorran
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()

        # Likelihood that strike fell within errorEllipse.
        self.error_ellipse_confidence = PerCent()

        # Length of major semi-axis (longest radius) of the error ellipse.
        self.error_ellipse_major_semi_axis = Length()

        # Length of minor semi-axis (shortest radius) of the error ellipse.
        self.error_ellipse_minor_semi_axis = Length()

        # The orientation of the major semi- axis in degrees from True North.
        self.error_ellipse_orientation = Bearing()

        # The polarity of the strike, with T meaning negative. About 90% of all lightning strokes are negative strokes,
        # meaning that they were initiated by a large concentration of negative charge in the cloud-base; this
        # tends to induce an area of positive charge on the ground.
        self.negative_polarity = True

        # Peak current of strike.
        self.peak_amplitude = CurrentFlow()
