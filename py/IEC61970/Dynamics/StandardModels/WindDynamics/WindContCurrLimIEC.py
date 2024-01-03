# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:35:41 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.PU import PU
from IEC61970.Dynamics.StandardModels.WindDynamics.WindTurbineType3or4IEC import WindTurbineType3or4IEC


class WindContCurrLimIEC(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.imax = PU()  # Maximum continuous current at the wind turbine terminals (i_max). It is type dependent parameter.
        self.imaxdip = PU()  # Maximum current during voltage dip at the wind turbine terminals (i_maxdip). It is project dependent parameter.
        self.kpqu = PU()  # Partial derivative of reactive current limit (K_pqu). It is type dependent parameter.
        self.mdfslim = True  # Limitation of type 3 stator current (M_DFSLim): false=0: total current limitation, true=1: stator current limitation. It is type dependent parameter.
        self.mqpri = True  # Prioritisation of q control during UVRT (M_qpri): true = 1: reactive power priority, false = 0: active power priority. It is project dependent parameter.
        self.tufiltcl = True  # Voltage measurement filter time constant (T_ufiltcl). It is type dependent parameter.
        self.upqumax = PU()  # Wind turbine voltage in the operation point where zero reactive current can be delivered (u_pqumax). It is type dependent parameter.
        self.wind_turbine_type_3or4_iec = WindTurbineType3or4IEC()  # Wind turbine type 3 or 4 model with which this wind control current limitation model is associated.
