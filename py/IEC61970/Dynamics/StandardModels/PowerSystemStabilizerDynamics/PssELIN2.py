# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics.PowerSystemStabilizerDynamics import \
    PowerSystemStabilizerDynamics


class PssElin2(PowerSystemStabilizerDynamics):
    """
    Power system stabilizer typically associated with ExcELIN2 (though PssIEEE2B or
    Pss2B can also be used).
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:20 PM
    """

    def __init__(self) -> None:
        """Constructor method"""
        super().__init__()
        self.apss: PU = PU(.1)  # Coefficient (a_PSS). Typical Value = 0.1.
        self.ks1: PU = PU(1)  # Gain (Ks1). Typical Value = 1.
        self.ks2: PU = PU(.1)  # Gain (Ks2). Typical Value = 0.1.
        self.ppss: PU = PU(.1)  # Coefficient (p_PSS) (>=0 and <=4). Typical Value = 0.1.
        self.psslim: PU = PU(.1)  # PSS limiter (psslim). Typical Value = 0.1.
        self.ts1: Seconds = Seconds(0)  # Time constant (Ts1). Typical Value = 0.
        self.ts2: Seconds = Seconds(1)  # Time constant (Ts2). Typical Value = 1.
        self.ts3: Seconds = Seconds(1)  # Time constant (Ts3). Typical Value = 1.
        self.ts4: Seconds = Seconds(.1)  # Time constant (Ts4). Typical Value = 0.1.
        self.ts5: Seconds = Seconds(0)  # Time constant (Ts5). Typical Value = 0.
        self.ts6: Seconds = Seconds(1)  # Time constant (Ts6). Typical Value = 1.
