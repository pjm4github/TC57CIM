# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindContQPQULimIEC(IdentifiedObject):
    """
    QP and QU limitation model.

    Reference: IEC Standard 61400-27-1 Section 5.6.5.10.
    @author: civanov
    @version: 1.0
    @created: 29-Dec-2023 11:24:20 PM
    """

    def __init__(self):
        super().__init__()
        self.tpfiltql = Seconds()  # Power measurement filter time constant for Q capacity (T_pfiltql)
        self.tufiltql = Seconds()  # Voltage measurement filter time constant for Q capacity (T_ufiltql)
        self.wind_turbine_type3or4_iec = WindTurbineType3or4IEC()
        # Wind generator type 3 or 4 model with which this QP and QU limitation model is associated