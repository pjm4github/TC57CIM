# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from datetime import datetime

from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType1or2Dynamics import WindTurbineType1or2Dynamics


class WindTurbineType1or2IEC(WindTurbineType1or2Dynamics):
    """
    Parent class supporting relationships to IEC wind turbines Type 1 and 2
    including their control models.
    
    Generator model for wind turbine of IEC Type 1 or Type 2 is a standard
    asynchronous generator model.
    
    Reference: IEC Standard 61400-27-1 Section 5.5.2 and Section 5.5.3.
    
    @author: ppbr003
    @version: 1.0
    @created: 29-Dec-2023 11:24:21 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
