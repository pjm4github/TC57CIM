# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from enum import Enum


class FrancisGovernorControlKind(Enum):
    """
    Governor control flag for Francis hydro model.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """
    MECHANIC_HYDRO_LIC_TACHO_ACCELERATOR = 1  # Mechanic-hydraulic regulator with tacho-accelerometer (Cflag = 1)
    MECHANIC_HYDRAULIC_TRANSIENT_FEEDBACK = 2  # Mechanic-hydraulic regulator with transient feedback (Cflag=2)
    ELECTROMECHANICAL_ELECTROHYDRAULIC = 3  # Electromechanical and electrohydraulic regulator (Cflag=3)
