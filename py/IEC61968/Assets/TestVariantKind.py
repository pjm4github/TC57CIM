# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum


class TestVariantKind(Enum):
    """
    A class to represent different test variant kinds.
    """

    SPECIMEN_OF_1_MM_THICKNESS_USED_IN_TESTING = 1  # "1MM"
    SPECIMEN_OF_2_MM_THICKNESS_USED_IN_TESTING = 2  # "2MM"
    TESTING_DONE_AT_TEMPERATURE_OF_MINUS_40_C = 3  # "MINUS40C"
    TESTING_DONE_AT_TEMPERATURE_OF_MINUS_30_C = 4  # "MINUS30C"
    TESTING_DONE_AT_TEMPERATURE_OF_0_C = 5  # "0C"
    TESTING_DONE_AT_TEMPERATURE_OF_25_C = 6  # "25C"
    TESTING_DONE_AT_TEMPERATURE_OF_30_C = 7  # "30C"
    TESTING_DONE_AT_TEMPERATURE_OF_40_C = 8  # "40C"
    TESTING_DONE_AT_TEMPERATURE_OF_100_C = 9  # "100C"
    MEASUREMENTS_TAKEN_AT_72_HOURS = 10  # "72HOURS"
    MEASUREMENTS_TAKEN_AT_164_HOURS = 11  # "164HOURS"
