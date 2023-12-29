# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from typing import Any

from IEC61970.Base.Core.Curve import Curve
from IEC62325.MarketOperations.ParticipantInterfaces.GeneratingBid import GeneratingBid
from IEC62325.MarketOperations.ReferenceData.RegisteredGenerator import RegisteredGenerator


class StartUpCostCurve(Curve):

    def __init__(self) -> None:
        super().__init__()
        self.registered_generators: RegisteredGenerator = RegisteredGenerator()
        self.generating_bid: GeneratingBid = GeneratingBid()