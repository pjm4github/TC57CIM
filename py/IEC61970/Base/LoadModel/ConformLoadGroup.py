# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:30:57 2024
from IEC61970.Base.LoadModel.ConformLoad import ConformLoad
from IEC61970.Base.LoadModel.ConformLoadSchedule import ConformLoadSchedule
from IEC61970.Base.LoadModel.LoadGroup import LoadGroup


class ConformLoadGroup(LoadGroup):
    """
    A group of loads conforming to an allocation pattern.
    @created 03-Jan-2024 10:44:40 PM
    """
    def __init__(self):
        super().__init__()
        # Conform loads assigned to this ConformLoadGroup
        self.energy_consumers = ConformLoad()  # Typical value as argument to the Java class method call
        # The ConformLoadSchedules in the ConformLoadGroup
        self.conform_load_schedules = ConformLoadSchedule()  # Typical value as argument to the Java class method call

