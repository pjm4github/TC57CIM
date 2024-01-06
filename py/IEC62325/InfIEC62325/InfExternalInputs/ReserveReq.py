from IEC62325.InfIEC62325.InfExternalInputs.ResourceGroupReq import ResourceGroupReq
from IEC62325.InfIEC62325.InfExternalInputs.SensitivityPriceCurve import SensitivityPriceCurve
from IEC62325.MarketOperations.MarketPlan.MarketProduct import MarketProduct


class ReserveReq(ResourceGroupReq):
    """
    Requirements for minimum amount of reserve and/or regulation to be supplied by
    a set of qualified resources.
    @updated 03-Jan-2024 1:50:34 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
        self.sensitivityPriceCurve = SensitivityPriceCurve()  # Creating an instance of SensitivityPriceCurve class and assigning it to the 'sensitivityPriceCurve' attribute
        self.marketProduct = MarketProduct()  # Creating an instance of MarketProduct class and assigning it to the 'marketProduct' attribute
