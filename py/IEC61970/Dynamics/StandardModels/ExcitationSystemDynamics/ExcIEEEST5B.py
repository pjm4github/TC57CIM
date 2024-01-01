# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds

from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcIeeeSt5B(ExcitationSystemDynamics):
    """
    The class represents IEEE Std 421.5-2005 type ST5B model. The Type ST5B
    excitation system is a variation of the Type ST1A model, with alternative
    overexcitation and underexcitation inputs and additional limits.

    Reference: IEEE Standard 421.5-2005 Section 7.5.

    Note: the block diagram in the IEEE 421.5 standard has input signal Vc and does
    not indicate the summation point with Vref. The implementation of the
    ExcIEEEST5B shall consider summation point with Vref.

    @author: pcha006
    @version: 1.0
    @created: 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.kc: PU = PU()  # Rectifier regulation factor (Kc). Typical Value = 0.004
        self.kr: PU = PU()  # Regulator gain (Kr). Typical Value = 200
        self.t1: Seconds = Seconds()  # Firing circuit time constant (T1). Typical Value = 0.004
        self.tb1: Seconds = Seconds()  # Regulator lag time constant (TB1). Typical Value = 6
        self.tb2: Seconds = Seconds()  # Regulator lag time constant (TB2). Typical Value = 0.01
        self.tc1: Seconds = Seconds()  # Regulator lead time constant (TC1). Typical Value = 0.8
        self.tc2: Seconds = Seconds()  # Regulator lead time constant (TC2). Typical Value = 0.08
        self.tob1: Seconds = Seconds()  # OEL lag time constant (TOB1). Typical Value = 2
        self.tob2: Seconds = Seconds()  # OEL lag time constant (TOB2). Typical Value = 0.08
        self.toc1: Seconds = Seconds()  # OEL lead time constant (TOC1). Typical Value = 0.1
        self.toc2: Seconds = Seconds()  # OEL lead time constant (TOC2). Typical Value = 0.08
        self.tub1: Seconds = Seconds()  # UEL lag time constant (TUB1). Typical Value = 10
        self.tub2: Seconds = Seconds()  # UEL lag time constant (TUB2). Typical Value = 0.05
        self.tuc1: Seconds = Seconds()  # UEL lead time constant (TUC1). Typical Value = 2
        self.tuc2: Seconds = Seconds()  # UEL lead time constant (TUC2). Typical Value = 0.1
        self.vrmax: PU = PU()  # Maximum voltage regulator output (VRMAX). Typical Value = 5
        self.vrmin: PU = PU()  # Minimum voltage regulator output (VRMIN). Typical Value = -4

