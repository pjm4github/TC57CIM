# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# facility_kind.py

from enum import Enum


class FacilityKind(Enum):
    SUBSTATION_HYDRO_PLANT = 1  # "SUBSTATIONHYDROPLANT"
    SUBSTATION_FOSSIL_PLANT = 2  # "SUBSTATIONFOSSILPLANT"
    SUBSTATION_NUCLEAR_PLANT = 3  # "SUBSTATIONNUCLEARPLANT"
    SUBSTATION_TRANSMISSION = 4  # "SUBSTATIONTRANSMISSION"
    SUBSTATION_SUB_TRANSMISSION = 5  # "SUBSTATIONSUBTRANSMISSION"
    SUBSTATION_DISTRIBUTION = 6  # "SUBSTATIONDISTRIBUTION"
    DISTRIBUTION_POLE_TOP = 7  # "DISTRIBUTIONPOLETOP"
