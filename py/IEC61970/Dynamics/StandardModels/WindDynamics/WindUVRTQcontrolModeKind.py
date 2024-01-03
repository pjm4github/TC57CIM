# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from enum import Enum

class WindUVRTQcontrolModeKind(Enum):
    MODE_0 = 0  # Voltage dependent reactive current injection (MqUVRT = 0)
    MODE_1 = 1  # Reactive current injection controlled as the pre-fault value plus an additional voltage dependent reactive current injection (MqUVRT = 1)
    MODE_2 = 2  # Reactive current injection controlled as the pre-fault value plus an additional voltage dependent reactive current injection during fault, and as the pre-fault value plus an additional constant reactive current injection post fault (MqUVRT = 2)
