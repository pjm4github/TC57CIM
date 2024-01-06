# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:30:57 2024
# NonConformLoadGroup.py

from IEC61970.Base.LoadModel.LoadGroup import LoadGroup
from IEC61970.Base.LoadModel.NonConformLoad import NonConformLoad
from IEC61970.Base.LoadModel.NonConformLoadSchedule import NonConformLoadSchedule


class NonConformLoadGroup(LoadGroup):
    """
    Loads that do not follow a daily and seasonal load variation pattern.
    @created 03-Jan-2024 10:44:40 PM
    """

    def __init__(self):
        super().__init__()
        """
        Constructor
        """
        self.non_conform_load_energy_consumers = NonConformLoad()  # NonConformLoad type
        # Conform loads assigned to this ConformLoadGroup
        
        self.non_conform_load_schedules = NonConformLoadSchedule()  # NonConformLoadSchedule type
        # The NonConformLoadSchedules in the NonConformLoadGroup

