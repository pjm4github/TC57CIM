# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC62325.MarketOperations.MarketOpCommon.MktLine import MktLine
from IEC62325.MarketOperations.MarketOpCommon.MktPowerTransformer import MktPowerTransformer
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.SecurityConstraints import SecurityConstraints
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionCapacity import TransmissionCapacity
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransmissionInterfaceRightEntitlement import \
    TransmissionInterfaceRightEntitlement
from IEC62325.MarketOperations.ReferenceData.FlowgatePartner import FlowgateValue
from IEC62325.MarketOperations.ReferenceData.FlowgateRelief import FlowgateRelief
from IEC62325.MarketOperations.ReferenceData.RegisteredInterTie import RegisteredInterTie
from IEC62325.MarketOperations.ReferenceData.SchedulingPoint import SchedulingPoint
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class Flowgate(PowerSystemResource):
    """
    A flowgate, is single or group of transmission elements intended to model MW
    flow impact relating to transmission limitations and transmission service usage.
    
    @created 28-Dec-2023 12:12:12 PM
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.direction: InterTieDirection = InterTieDirection()
        self.export_mw_rating: ActivePower = ActivePower()
        self.import_mw_rating: ActivePower = ActivePower()
        self.flowgate_relief: FlowgateRelief = FlowgateRelief()
        self.inter_tie_results: InterTieResults = InterTieResults()
        self.ftrs: FTR = FTR()
        self.inter_tie: SchedulingPoint = SchedulingPoint()
        self.contract_distribution_factor: ContractDistributionFactor = ContractDistributionFactor()
        self.registered_inter_tie: RegisteredInterTie = RegisteredInterTie()
        self.to_sub_control_area: SubControlArea = SubControlArea()
        self.from_sub_control_area: SubControlArea = SubControlArea()
        self.flowgate_value: FlowgateValue = FlowgateValue()
        self.constraint_results: ConstraintResults = ConstraintResults()
        self.security_constraints: SecurityConstraints = SecurityConstraints()
        self.transmission_right_entitlement: TransmissionInterfaceRightEntitlement = TransmissionInterfaceRightEntitlement()
        self.transmission_capacity: TransmissionCapacity = TransmissionCapacity()
        self.mkt_line: MktLine = MktLine()
        self.mkt_power_transformer: MktPowerTransformer = MktPowerTransformer()
