# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC61970.Base.Domain.DateTime import DateTime


class ScadaInformation:
    """
    Contains information about the update from SCADA.
    
    @created 27-Dec-2023 3:31:38 PM
    """

    def __init__(self) -> None:
        """
        Constructor for the SCADAInformation class.
        """
        # * time of the update from SCADA
        self.time_stamp: DateTime = DateTime()
