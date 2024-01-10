# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from enum import Enum

class WindLookupTableFunctionKind(Enum):
    """
    Function of the lookup table.
    """
    # Power versus speed change (negative slip) lookup table (p<sub>err</sub>(deltaomega)).
    # It is used for rotor resistance control model, IEC 61400-27-1, section 5.6.5.3.
    PRR = 1

    # Power vs. speed lookup table (omega(p)).
    # It is used for P control model type 3, IEC 61400-27-1, section 5.6.5.4.
    OMEGA_P = 2

    # Lookup table for voltage dependency of active current limits (i<sub>epmax</sub>(u<sub>WT</sub>)).
    # It is used for current limitation model, IEC 61400-27-1, section 5.6.5.8.
    IPMAX = 3

    # Lookup table for voltage dependency of reactive current limits (i<sub>eqmax</sub>(u<sub>WT</sub>)).
    # It is used for current limitation model, IEC 61400-27-1, section 5.6.5.8.
    IQMAX = 4

    # Power vs. frequency lookup table (p<sub>WPbias</sub>(f)).
    # It is used for wind power plant frequency and active power control model, IEC 61400-27-1, Annex D.
    PWP = 5

    # Crowbar duration versus voltage variation look-up table (T<sub>CW</sub>(du)).
    # It is case dependent parameter. It is used for type 3B generator set model, IEC 61400-27-1, section 5.6.3.3.
    TCWDU = 6

    # Lookup table to determine the duration of the power reduction after a voltage dip, depending on the size of the voltage dip (T<sub>d</sub>(u<sub>WT</sub>)).
    # It is type dependent parameter. It is used for pitch control power model, IEC 61400-27-1, section 5.6.5.1.
    TDUWT = 7

    # Lookup table for active power dependency of reactive power maximum limit (q<sub>maxp</sub>(p)).
    # It is used for QP and QU limitation model, IEC 61400-27-1, section 5.6.5.10.
    QMAXP = 8

    # Lookup table for active power dependency of reactive power minimum limit (q<sub>minp</sub>(p)).
    # It is used for QP and QU limitation model, IEC 61400-27-1, section 5.6.5.10.
    QMINP = 9

    # Lookup table for voltage dependency of reactive power maximum limit (q<sub>maxu</sub>(p)).
    # It is used for QP and QU limitation model, IEC 61400-27-1, section 5.6.5.10.
    QMAXU = 10

    # Lookup table for voltage dependency of reactive power minimum limit (q<sub>minu</sub>(p)).
    # It is used for QP and QU limitation model, IEC 61400-27-1, section 5.6.5.10.
    QMINU = 11

    # Disconnection time versus over voltage lookup table (T<sub>uover</sub>(u<sub>WT</sub>)).
    # It is used for grid protection model, IEC 61400-27-1, section 5.6.6.
    TUOVER = 12

    # Disconnection time versus under voltage lookup table (T<sub>uunder</sub>(u<sub>WT</sub>)).
    # It is used for grid protection model, IEC 61400-27-1, section 5.6.6.
    TUUNDER = 13

    # Disconnection time versus over frequency lookup table (T<sub>fover</sub>(f<sub>WT</sub>)).
    # It is used for grid protection model, IEC 61400-27-1, section 5.6.6.
    TFOVER = 14

    # Disconnection time versus under frequency lookup table (T<sub>funderr</sub>(f<sub>WT</sub>)).
    # It is used for grid protection model, IEC 61400-27-1, section 5.6.6.
    TFUNDER = 15

    # Look up table for the UQ static mode (q<sub>WP</sub>(u<sub>err</sub>)).
    # It is used for voltage and reactive power control model, IEC 61400-27-1, Annex D.
    QWP = 16
