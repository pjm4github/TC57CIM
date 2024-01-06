from IEC62325.MarketOperations.ReferenceData.RegisteredGenerator import RegisteredGenerator
from IEC62325.MarketOperations.ReferenceData.RegisteredLoad import RegisteredLoad


class AuxiliaryObject:
    """
    Models Auxiliary Values.
    """
    def __init__(self):
        self.registered_load = RegisteredLoad()  # Associated RegisteredLoad
        self.registered_generator = RegisteredGenerator()  # Associated RegisteredGenerator
