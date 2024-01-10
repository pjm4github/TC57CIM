# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:03:17 2023
from enum import Enum

class InputSignalKind(Enum):
    """
    Input signal type.  In Dynamics modelling, commonly represented by j parameter.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """
    
    ROTOR_SPEED = 1
    ROTOR_ANGULAR_FREQUENCY_DEVIATION = 2
    BUS_FREQUENCY = 3
    BUS_FREQUENCY_DEVIATION = 4
    GENERATOR_ELECTRICAL_POWER = 5
    GENERATOR_ACCELERATING_POWER = 6
    BUS_VOLTAGE = 7
    BUS_VOLTAGE_DERIVATIVE = 8
    BRANCH_CURRENT = 9
    FIELD_CURRENT = 10
