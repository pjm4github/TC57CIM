# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.OrganisationRole import OrganisationRole
from IEC61968.Customers.CustomerAgreement import CustomerAgreement
from IEC61968.InfIEC61968.InfCommon.BankAccount import BankAccount
from IEC61968.Metering.UsagePoint import UsagePoint
from IEC61968.PaymentMetering.SupplierKind import SupplierKind


class ServiceSupplier(OrganisationRole):

    def __init__(self):
        super().__init__()
        self.issuer_identification_number = ""
        self.kind = SupplierKind()
        self.bank_accounts = BankAccount()
        self.usage_points = UsagePoint()
        self.customer_agreements = CustomerAgreement()

