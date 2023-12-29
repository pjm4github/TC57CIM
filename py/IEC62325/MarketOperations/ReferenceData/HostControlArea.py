# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023

from typing import Optional

from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Domain.Frequency import Frequency
from IEC62325.InfIEC62325.InfFinancial.ControlAreaOperator import ControlAreaOperator
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.SysLoadDistributionFactor import SysLoadDistributionFactor
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.TransferInterface import TransferInterface
from IEC62325.MarketOperations.MktDomain.AreaControlMode import AreaControlMode
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class HostControlArea(PowerSystemResource):
    """
    A HostControlArea has a set of tie points and a set of generator controls (i.e., AGC). It also has a total load,
    including transmission and distribution losses.
    @created 28-Dec-2023 12:15:02 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.area_control_mode: AreaControlMode = AreaControlMode.CF  # The area's present control mode
        """
        The area's present control mode: (CF = constant frequency) or (CTL = constant tie-line) or (TLB = tie-line bias) or 
        (OFF = off control).
        """
        self.freq_set_point: Frequency = Frequency()  # The present power system frequency set point for automatic generation control
        self.frequency_bias_factor: float = 0.0  # The control area's frequency bias factor, in MW/0.1 Hz, for automatic generation control (AGC)
        self.adjacent_ca_set: AdjacentCASet = AdjacentCASet()
        self.controls: ControlAreaOperator = ControlAreaOperator()  # A ControlAreaCompany controls a ControlArea.
        self.flowgate: Flowgate = Flowgate()
        self.cnode_distribution_factor: CnodeDistributionFactor = CnodeDistributionFactor()
        self.sub_control_areas: SubControlArea = SubControlArea()  # The interchange area may operate as a control area
        self.bid_self_sched: BidSelfSched = BidSelfSched()
        self.loss_clearing_results: LossClearingResults = LossClearingResults()
        self.transfer_interface: TransferInterface = TransferInterface()
        self.sys_load_distribution_factor: SysLoadDistributionFactor = SysLoadDistributionFactor()
        self.registered_resource: RegisteredResource = RegisteredResource()
