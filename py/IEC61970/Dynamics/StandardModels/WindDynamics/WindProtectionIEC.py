# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType1or2IEC import WindTurbineType1or2IEC
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindProtectionIEC(IdentifiedObject):
    """The grid protection model includes protection against over and under voltage,
    and against over and under frequency.

    Reference: IEC Standard 61400-27-1 Section 5.6.6.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.dfimax: PU = PU()
        # Maximum rate of change of frequency (<i>dF</i><sub>max</sub>). It is   type dependent parameter.

        self.fover: PU = PU()
        # Wind turbine over frequency protection activation threshold        (<i>f</i><sub>over</sub>). It is project dependent parameter.

        self.funder: PU = PU()
        # Wind turbine under frequency protection activation threshold        (<i>f</i><sub>under</sub>). It is project dependent parameter.

        self.mzc: bool = False
        # Zero crossing measurement mode (<i>Mzc</i>). True = 1 if the WT protection        system uses zero crossings to detect frequency - otherwise false = 0. It is        type dependent parameter.

        self.tfma: Seconds = Seconds()
        # Time interval of moving average window (<i>TfMA</i>). It is type dependent        parameter.

        self.uover: PU = PU()
        # Wind turbine over-voltage protection activation threshold        (<i>u</i><sub>over</sub>). It is project dependent parameter.

        self.uunder: PU = PU()
        # Wind turbine under voltage protection activation threshold        (<i>u</i><sub>under</sub>). It is project dependent parameter.

        self.wind_turbine_type_3_or_4_iec: Optional[WindTurbineType3or4IEC] = WindTurbineType3or4IEC()
        # Wind generator type 3 or 4 model with which this wind turbine protection model is associated.

        self.wind_turbine_type_1_or_2_iec: Optional[WindTurbineType1or2IEC] = WindTurbineType1or2IEC()
        # Wind generator type 1 or 2 model with which this wind turbine protection model is associated.
