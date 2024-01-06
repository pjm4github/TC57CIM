from IEC61970.Base.Core.Curve import Curve  # Importing Curve class from IEC61970.Base.Core module

class SensitivityPriceCurve(Curve):
    """
    Optionally, this curve expresses elasticity of the associated requirement. For
    example, used to reduce requirements when clearing price exceeds reasonable
    values when the supply quantity becomes scarce. For example, a single point
    value of $1000/MW for a spinning reserve will cause a reduction in the required
    spinning reserve.
    X axis is constrained quantity (e.g., MW)
    Y1 axis is money per constrained quantity
    @created 28-Dec-2023 7:58:37 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
