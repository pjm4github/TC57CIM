# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindGenTurbineType2IEC import WindGenTurbineType2IEC


class WindPitchContPowerIEC(IdentifiedObject):
    """
    Pitch control power model.
    Reference: IEC Standard 61400-27-1 Section 5.6.5.1.
    @author civanov
    @version 1.0
    @created 29-Dec-2023 11:24:21 PM
    """

    def __init__(self) -> None:
        # Rate limit for increasing power (d<p>max</p>).    It is type dependent parameter.
        super().__init__()
        self.dp_max: PU = PU()

        # Rate limit for decreasing power (d<p>min</p>).        It is type dependent parameter.
        self.dp_min: PU = PU()

        # Minimum power setting (pmin).       It is type dependent parameter.
        self.p_min: PU = PU()

        # If p<sub>init < /sub> < p<sub>set < /sub> then power will be ramped        down to pmin. It is (p<sub>set< /sub>) in the IEC 61400-        27-1. It is type dependent parameter.
        self.p_set: PU = PU()

        # Lag time constant (T<sub>1</sub>).        It is type dependent parameter.
        self.t1: Seconds = Seconds(1.0)

        # Voltage measurement time constant (T<sub>r</sub>).        It is type dependent parameter.
        self.tr: Seconds = Seconds(1.0)

        # Dip detection threshold (u<sub>UVRT</sub>).        It is type dependent parameter.
        self.uuvrt: PU = PU()

        # Wind turbine type 2 model with which this Pitch control power model is        associated.
        self.wind_gen_turbine_type2_iec: Optional[WindGenTurbineType2IEC] = WindGenTurbineType2IEC()
