# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 16:30:57 2024
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class LoadResponseCharacteristic(IdentifiedObject):
    """
    Models the characteristic response of the load demand due to changes in system conditions such as voltage and frequency.
    This is not related to demand response.
    If LoadResponseCharacteristic.exponentModel is True, the voltage exponents are specified and used to calculate:
    
    Active power component = Pnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.pVoltageExponent
    Reactive power component = Qnominal * (Voltage/cim:BaseVoltage.nominalVoltage) ** cim:LoadResponseCharacteristic.qVoltageExponent
    Where * means "multiply" and ** is "raised to power of".
    @ author kdd
    @ version 1.0
    @created 03-Jan-2024 10:44:40 PM
    """

    def __init__(self):
        super().__init__()
        """
        Indicates the exponential voltage dependency model is to be used. 
        If false, the coefficient model is to be used. 
        The exponential voltage dependency model consist of the attributes
        - pVoltageExponent
        - qVoltageExponent. 
        The coefficient model consist of the attributes
        - pConstantImpedance
        - pConstantCurrent
        - pConstantPower
        - qConstantImpedance
        - qConstantCurrent
        - qConstantPower.
        The sum of pConstantImpedance, pConstantCurrent and pConstantPower shall equal 1.
        The sum of qConstantImpedance, qConstantCurrent and qConstantPower shall equal 1.
        """
        self.exponent_model = False
        self.p_constant_current = 0.0  # Portion of active power load modeled as constant current.
        self.p_constant_impedance = 0.0  # Portion of active power load modeled as constant impedance.
        self.p_constant_power = 0.0  # Portion of active power load modeled as constant power.
        self.p_frequency_exponent = 0.0  # Exponent of per unit frequency effecting active power.
        self.p_voltage_exponent = 0.0  # Exponent of per unit voltage effecting real power.
        self.q_constant_current = 0.0  # Portion of reactive power load modeled as constant current.
        self.q_constant_impedance = 0.0  # Portion of reactive power load modeled as constant impedance.
        self.q_constant_power = 0.0  # Portion of reactive power load modeled as constant power.
        self.q_frequency_exponent = 0.0  # Exponent of per unit frequency effecting reactive power.
        self.q_voltage_exponent = 0.0  # Exponent of per unit voltage effecting reactive power.
