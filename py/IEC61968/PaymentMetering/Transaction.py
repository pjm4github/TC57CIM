# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.Meter import Meter
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.LineDetail import LineDetail
from CIM_STD_PYTHON.TC57CIM.IEC61968.PaymentMetering.TransactionKind import TransactionKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.RealEnergy import RealEnergy


class Transaction(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.diverse_reference = ""
        self.donor_reference = ""
        self.kind = TransactionKind.SERVICE_CHARGE_PAYMENT
        self.line = LineDetail()
        self.receiver_reference = ""
        self.reversed_id = ""
        self.service_units_energy = RealEnergy()
        self.service_units_error = RealEnergy()
        self.meter = Meter()
