# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from typing import Optional

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Dynamics.StandardModels.ExcitationSystemDynamics.ExcitationSystemDynamics import ExcitationSystemDynamics


class ExcSt1A(ExcitationSystemDynamics):
    """
    Modification of an old IEEE ST1A static excitation system without
    overexcitation limiter (OEL) and underexcitation limiter (UEL).
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:18 PM
    """

    def __init__(self) -> None:
        """
        Exciter output current limit reference (Ilr). Typical Value = 0.
        """
        super().__init__()
        self.ilr: PU = PU(0)

        """
        Voltage regulator gain (Ka). Typical Value = 190.
        """
        self.ka: PU = PU(190)

        """
        Rectifier loading factor proportional to commutating reactance (Kc). Typical Value = 0.05.
        """
        self.kc: PU = PU(0.05)

        """
        Excitation control system stabilizer gains (Kf). Typical Value = 0.
        """
        self.kf: PU = PU(0)

        """
        Exciter output current limiter gain (Klr). Typical Value = 0.
        """
        self.klr: PU = PU(0)

        """
        Voltage regulator time constant (Ta). Typical Value = 0.02.
        """
        self.ta: Seconds = Seconds(0.02)

        """
        Voltage regulator time constant (Tb). Typical Value = 10.
        """
        self.tb: Seconds = Seconds(10)

        """
        Voltage regulator time constant (Tb1). Typical Value = 0.
        """
        self.tb1: Seconds = Seconds(0)

        """
        Voltage regulator time constant (Tc). Typical Value = 1.
        """
        self.tc: Seconds = Seconds(1)

        """
        Voltage regulator time constant (Tc1). Typical Value = 0.
        """
        self.tc1: Seconds = Seconds(0)

        """
        Excitation control system stabilizer time constant (Tf). Typical Value = 1.
        """
        self.tf: Seconds = Seconds(1)

        """
        Maximum voltage regulator output (Vamax). Typical Value = 999.
        """
        self.vamax: PU = PU(999)

        """
        Minimum voltage regulator output (Vamin). Typical Value = -999.
        """
        self.vamin: PU = PU(-999)

        """
        Maximum voltage regulator input limit (Vimax). Typical Value = 999.
        """
        self.vimax: PU = PU(999)

        """
        Minimum voltage regulator input limit (Vimin). Typical Value = -999.
        """
        self.vimin: PU = PU(-999)

        """
        Maximum voltage regulator outputs (Vrmax). Typical Value = 7.8.
        """
        self.vrmax: PU = PU(7.8)

        """
        Minimum voltage regulator outputs (Vrmin). Typical Value = -6.7.
        """
        self.vrmin: PU = PU(-6.7)

        """
        Excitation xfmr effective reactance (Xe). Typical Value = 0.04.
        """
        self.xe: PU = PU(0.04)
