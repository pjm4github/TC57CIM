# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Analog classes representing oil fluid test analysis result
from enum import Enum


class OilAnalysisFluidAnalogKind(Enum):
    # Acid neutralization number (in milligram of KOH/gram)
    ACID_NUMBER = 1
    # Interfacial tension (in dyne/centimetre or milliNewton/metre, which are the same)
    INTERFACIAL_TENSION = 2
    # Dielectric breakdown, for electrode gap size and temperature specified by selected standard  (in kV)
    DIELECTRIC_BREAKDOWN = 3
    # Fluid power factor at specified temperature (in percent). Commonly used in the US.
    POWER_FACTOR_PERCENT = 4
    # Fluid dissipation factor in absolute value, not a percentage
    DISSIPATION_FACTOR = 5
    # Fluid dissipation factor (in percent). Commonly used in Asia
    DISSIPATION_FACTOR_PERCENT = 6
    # 2,6-ditertiary-butyl phenol (DBP) oxidation inhibitor concentration (in percent by weight)
    OXIDATION_INHIBITOR_DBP = 7
    # 2,6-ditertiarybutyl para-cresol (DBPC) oxidation inhibitor concentration (in percent by weight)
    OXIDATION_INHIBITOR_DBPC = 8
    # 2,6-ditertiary-butyl para-cresol and 2,6-ditertiary-butyl phenol concentration (in percent by weight)
    OXIDATION_INHIBITOR_D2668 = 9
    # Dibenzyl disulfide (DBDS) concentration (in ppm, specifically in milligram/kilogram)
    ADDITIVE_DBDS = 10
    # Specific gravity corrected to 15 C. Also known as relative density
    SPECIFIC_GRAVITY = 11
    # Density (in gram/millilitre)
    DENSITY = 12
    # Fire point (in C)
    FIRE_POINT = 13
    # Flash point (in C) determined via open cup test
    FLASH_POINT_OPEN_CUP = 14
    # Flash point (in C) determined via closed cup test
    FLASH_POINT_CLOSED_CUP = 15
    # Pour point (in C)
    POUR_POINT = 16
    # Pour point (in C) determined by automatic method
    POUR_POINT_AUTOMATIC = 17
    # Kinematic viscosity (in millimetre2/second)
    KINEMATIC_VISCOSITY = 18
    # Static electrification tendency (in microcoulombs per metre3)
    STATIC_ELECTRIFICATION = 19
    # Resistivity at 90 C (in gigohm-metre)
    RESISTIVITY = 20
    # Total passivator content (in milligram/kilogram)
    PASSIVATOR_CONTENT = 21
    # Irgamet 39 metal passivator content (in ppm, specifically milligram/kilogram)
    PASSIVATOR_IRGAMET39 = 22
    # Metal passivator TTA (Irgamet39 in solid form) content (in milligram/kilogram)
    PASSIVATOR_TTA = 23
    # Metal passivator BTA content (in milligram/kilogram)
    PASSIVATOR_BTA = 24
    # Sediment and sludge (in percent)
    SEDIMENT_AND_SLUDGE_PERCENT = 25
    # Concentration of carbonyl compounds (aldehydes and ketones) determined using infrared spectroscopy (in percent)
    CARBONYL = 26
    # Concentration of aromatic compounds determined using infrared spectroscopy (in percent)
    AROMATICS = 27
    # Measure of oxidation stability (in hours)
    OXIDATION = 28
    # Sludge (in percent by mass)
    SLUDGE = 29
    # Soluble acids (in milligram of KOH/gram)
    SOLUBLE_ACIDS = 30
    # Volatile acids (in milligram of KOH/gram)
    VOLATILE_ACIDS = 31
    # Total acids (soluble plus volatile) (in milligram of KOH/gram)
    TOTAL_ACIDS = 32
    # Oxidation induction time (in hours)
    INDUCTION_TIME = 33
    # Amount of inhibitor used in oxidation stability test performed according to IEC 61125, method C (in milligram/kilogram)
    INHIBITOR_61125_METHOD_C = 34
    # Duration of oxidation stability test performed according to IEC 61125, method C
    DURATION_61125_METHOD_C = 35
    # Characterization of the carbon-type composition of insulating oils by petroleum origin
    PETROLEUM_ORIGIN = 36
