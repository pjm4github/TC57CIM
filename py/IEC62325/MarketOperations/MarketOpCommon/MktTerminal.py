# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.ReferenceData.Flowgate import Flowgate
from IEC61970.Base.Core import Terminal


class MktTerminal(Terminal):
    """
    Subclass of IEC61970:Core:Terminal.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """
    def __init__(self):
        super().__init__()
        self.flow_gate = Flowgate()
