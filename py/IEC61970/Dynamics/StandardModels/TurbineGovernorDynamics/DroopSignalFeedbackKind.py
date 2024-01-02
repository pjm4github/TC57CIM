# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:08:39 2023
from enum import Enum

class DroopSignalFeedbackKind(Enum):
    """ Governor droop signal feedback source.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:24:17 PM
    """

    # Electrical power feedback (connection indicated as 1 in the block diagrams of
    # models, e.g. GovCT1, GovCT2).
    ELECTRICAL_POWER = 1

    # No droop signal feedback, is isochronous governor.
    NONE = 0

    # Fuel valve stroke feedback (true stroke) (connection indicated as 2 in the
    # block diagrams of model, e.g. GovCT1, GovCT2).
    FUEL_VALVE_STROKE = 2

    # Governor output feedback (requested stroke) (connection indicated as 3 in the
    # block diagrams of models, e.g. GovCT1, GovCT2).
    GOVERNOR_OUTPUT = 3
