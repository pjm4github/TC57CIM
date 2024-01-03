# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.WindDynamics.WindGenType3IEC import WindGenType3IEC


class WindGenType3bIEC(WindGenType3IEC):
    """
    IEC Type 3B generator set model.
    
    Reference: IEC Standard 61400-27-1 Section 5.6.3.3.
    @author: civanov
    @version: 1.0
    @created: 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.mwtcwp: bool  = False  # Crowbar control mode (M<sub>WTcwp</sub>).
        self.tg: Seconds = Seconds()  # Current generation Time constant (T<sub>g</sub>). It is type dependent parameter.
        self.two: Seconds = Seconds()  # Time constant for crowbar washout filter (T<sub>wo</sub>). It is case dependent parameter.
