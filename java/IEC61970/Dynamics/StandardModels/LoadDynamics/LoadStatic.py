# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from enum import Enum


class StaticLoadModelKind(Enum):
    CONSTANT_Z = 1
    EXPONENTIAL = 2
    ZIP2 = 3


class LoadStatic:
    ep1: float  # First term voltage exponent for active power (Ep1).
    ep2: float  # Second term voltage exponent for active power (Ep2).
    ep3: float  # Third term voltage exponent for active power (Ep3).
    eq1: float  # First term voltage exponent for reactive power (Eq1).
    eq2: float  # Second term voltage exponent for reactive power (Eq2).
    eq3: float  # Third term voltage exponent for reactive power (Eq3).
    kp1: float  # First term voltage coefficient for active power (Kp1).
    kp2: float  # Second term voltage coefficient for active power (Kp2).
    kp3: float  # Third term voltage coefficient for active power (Kp3).
    kp4: float  # Frequency coefficient for active power (Kp4).
    kpf: float  # Frequency deviation coefficient for active power (Kpf).
    kq1: float  # First term voltage coefficient for reactive power (Kq1).
    kq2: float  # Second term voltage coefficient for reactive power (Kq2).
    kq3: float  # Third term voltage coefficient for reactive power (Kq3).
    kq4: float  # Frequency coefficient for reactive power (Kq4).
    kqf: float  # Frequency deviation coefficient for reactive power (Kqf).
    static_load_model_type: StaticLoadModelKind
    load_aggregate: 'LoadAggregate'  # Aggregate load to which this aggregate static load belongs.

    def __init__(self) -> None:
        pass
