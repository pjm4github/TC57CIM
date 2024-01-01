# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:59:32 2023
from datetime import timedelta

from IEC61970.Base.Domain.PU import PU
from IEC61970.Base.Domain.Seconds import Seconds
from typing import Type

from IEC61970.Dynamics.StandardModels.DiscontinuousExcitationControlDynamics.DiscontinuousExcitationControlDynamics import \
    DiscontinuousExcitationControlDynamics


class DiscExcContIEEEDEC2A(DiscontinuousExcitationControlDynamics):
    """
    The class represents IEEE Type DEC2A model for the discontinuous excitation 
    control. This system provides transient excitation boosting via an open-loop 
    control as initiated by a trigger signal generated remotely.

    Reference: IEEE Standard 421.5-2005 Section 12.3.
    """
    def __init__(self) -> None:
        """
        Discontinuous controller time constant (T_D1).
        """
        super().__init__()
        self.td1: Seconds = Seconds()  # time constant T_D1.
        self.td2:  Seconds = Seconds()  # time constant T_D2.
        self.vdmax: PU = PU()  # limiter V_DMAX.
        self.vdmin: PU = PU()  # limiter V_DMIN.
        self.vk: PU = PU()  # input reference V_K.
