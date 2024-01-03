# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:51:45 2023
from IEC61970.Dynamics.UserDefinedModels.AsynchronousMachineUserDefined import AsynchronousMachineUserDefined
from IEC61970.Dynamics.UserDefinedModels.DiscontinuousExcitationControlUserDefined import \
    DiscontinuousExcitationControlUserDefined
from IEC61970.Dynamics.UserDefinedModels.ExcitationSystemUserDefined import ExcitationSystemUserDefined
from IEC61970.Dynamics.UserDefinedModels.LoadUserDefined import LoadUserDefined
from IEC61970.Dynamics.UserDefinedModels.MechanicalLoadUserDefined import MechanicalLoadUserDefined
from IEC61970.Dynamics.UserDefinedModels.OverexcitationLimiterUserDefined import OverexcitationLimiterUserDefined
from IEC61970.Dynamics.UserDefinedModels.PFVArControllerType1UserDefined import PFVArControllerType1UserDefined
from IEC61970.Dynamics.UserDefinedModels.PFVArControllerType2UserDefined import PFVArControllerType2UserDefined
from IEC61970.Dynamics.UserDefinedModels.PowerSystemStabilizerUserDefined import PowerSystemStabilizerUserDefined
from IEC61970.Dynamics.UserDefinedModels.SynchronousMachineUserDefined import SynchronousMachineUserDefined
from IEC61970.Dynamics.UserDefinedModels.TurbineGovernorUserDefined import TurbineGovernorUserDefined
from IEC61970.Dynamics.UserDefinedModels.TurbineLoadControllerUserDefined import TurbineLoadControllerUserDefined
from IEC61970.Dynamics.UserDefinedModels.UnderexcitationLimiterUserDefined import UnderexcitationLimiterUserDefined
from IEC61970.Dynamics.UserDefinedModels.VoltageAdjusterUserDefined import VoltageAdjusterUserDefined
from IEC61970.Dynamics.UserDefinedModels.VoltageCompensatorUserDefined import VoltageCompensatorUserDefined


class ProprietaryParameterDynamics:
    """
    Supports definition of one or more parameters of several different datatypes
    for use by proprietary user-defined models.  NOTE: This class does not inherit
    from IdentifiedObject since it is not intended that a single instance of it be
    referenced by more than one proprietary user-defined model instance.
    @author ppbr003
    @version 1.0
    @created 29-Dec-2023 11:21:46 PM
    """

    def __init__(self):
        self.boolean_parameter_value = True  # Used for boolean parameter value
        self.float_parameter_value = 0.0  # Used for floating point parameter value
        self.integer_parameter_value = 0  # Used for integer parameter value
        self.parameter_number = 0  # Sequence number of the parameter among the set of parameters associated with the related proprietary user-defined model
        self.load_user_defined = LoadUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.voltage_compensator_user_defined = VoltageCompensatorUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.pf_var_controller_type2_user_defined = PFVArControllerType2UserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.voltage_adjuster_user_defined = VoltageAdjusterUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.pf_var_controller_type1_user_defined = PFVArControllerType1UserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.discontinuous_excitation_control_user_defined = DiscontinuousExcitationControlUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.power_system_stabilizer_user_defined = PowerSystemStabilizerUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.underexcitation_limiter_user_defined = UnderexcitationLimiterUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.overexcitation_limiter_user_defined = OverexcitationLimiterUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.excitation_system_user_defined = ExcitationSystemUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.mechanical_load_user_defined = MechanicalLoadUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.turbine_load_controller_user_defined = TurbineLoadControllerUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.turbine_governor_user_defined = TurbineGovernorUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.asynchronous_machine_user_defined = AsynchronousMachineUserDefined()  # Proprietary user-defined model with which this parameter is associated
        self.synchronous_machine_user_defined = SynchronousMachineUserDefined()  # Proprietary user-defined model with which this parameter
