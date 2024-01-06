from IEC61970.Base.Core.Curve import Curve  # Importing Curve class from IEC61970.Base.Core module
from IEC62325.InfIEC62325.InfExternalInputs.ReserveReq import ReserveReq


class ReserveReqCurve(Curve):
    """
    A curve relating reserve requirement versus time, showing the values of a
    specific reserve requirement for each unit of the period covered. The curve
    can be based on "absolute" time or on "normalized' time.
    X is time, typically expressed in absolute time
    Y1 is reserve requirement, typically expressed in MW
    @updated 03-Jan-2024 1:50:35 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
        self.reserveReq = ReserveReq()  # Creating an instance of ReserveReq
        # class and assigning it to the 'reserveReq' attribute
