# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from IEC61968.Common.Agreement import Agreement
from IEC62325.InfIEC62325.InfFinancial.Marketer import Marketer
from IEC62325.InfIEC62325.InfFinancial.GenerationProvider import GenerationProvider

class EnergyProduct(Agreement):

    def __init__(self) -> None:
        super().__init__()
        self.resold_by_marketer: Marketer = Marketer()
        self.generation_provider: GenerationProvider = GenerationProvider()
        self.title_held_by_marketer: Marketer = Marketer()
