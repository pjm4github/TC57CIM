# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Dynamics.StandardModels.LoadDynamics.LoadAggregate import LoadAggregate
from IEC61970.Dynamics.StandardModels.LoadDynamics.StaticLoadModelKind import StaticLoadModelKind


class LoadStatic(IdentifiedObject):

    def __init__(self) -> None:
        # First term voltage exponent for active power (Ep1).  Used only when .
        # staticLoadModelType = exponential.
        super().__init__()
        self.ep1 = 1.0

        # Second term voltage exponent for active power (Ep2).  Used only when .
        # staticLoadModelType = exponential.
        self.ep2 = 0.1

        # Third term voltage exponent for active power (Ep3).  Used only when .
        # staticLoadModelType = exponential.
        self.ep3 = 1.0

        # First term voltage exponent for reactive power (Eq1).  Used only when .
        # staticLoadModelType = exponential.
        self.eq1 = 1.0

        # Second term voltage exponent for reactive power (Eq2).  Used only when .
        # staticLoadModelType = exponential.
        self.eq2 = 0.1

        # Third term voltage exponent for reactive power (Eq3).  Used only when .
        # staticLoadModelType = exponential.
        self.eq3 = 0.1

        # First term voltage coefficient for active power (Kp1).  Not used when .
        # staticLoadModelType = constantZ.
        self.kp1 = 1.0

        # Second term voltage coefficient for active power (Kp2).  Not used when .
        # staticLoadModelType = constantZ.
        self.kp2 = 1.0

        # Third term voltage coefficient for active power (Kp3).  Not used when .
        # staticLoadModelType = constantZ.
        self.kp3 = 0.1

        # Frequency coefficient for active power (Kp4).  Must be non-zero when .
        # staticLoadModelType = ZIP2.  Not used for all other values of .
        # staticLoadModelType.
        self.kp4 = 0.0

        # Frequency deviation coefficient for active power (Kpf).  Not used when .
        # staticLoadModelType = constantZ.
        self.kpf = 0.0

        # First term voltage coefficient for reactive power (Kq1).  Not used when .
        # staticLoadModelType = constantZ.
        self.kq1 = 1.0

        # Second term voltage coefficient for reactive power (Kq2).  Not used when .
        # staticLoadModelType = constantZ.
        self.kq2 = 0.0

        # Third term voltage coefficient for reactive power (Kq3).  Not used when .
        # staticLoadModelType = constantZ.

        self.kq3 = 0.0

        # Frequency coefficient for reactive power (Kq4).  Must be non-zero when .
        # staticLoadModelType = ZIP2.  Not used for all other values of .
        # staticLoadModelType.
        self.kq4 = 0.0

        # Frequency deviation coefficient for reactive power (Kqf).  Not used when .
        # staticLoadModelType = constantZ.
        self.kqf = 0.0

        # Type of static load model.  Typical Value = constantZ.
        self.static_load_model_kind = StaticLoadModelKind.CONSTANT_Z

        # Aggregate load to which this aggregate static load belongs.
        self.load_aggregate = LoadAggregate()
