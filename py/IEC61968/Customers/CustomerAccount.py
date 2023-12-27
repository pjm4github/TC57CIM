from IEC61968.Common.Document import Document
from IEC61968.Customers.AccountNotification import AccountNotification
from IEC61968.Customers.CustomerAgreement import CustomerAgreement
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoice import ErpInvoice
from IEC61970.Base.Domain.Money import Money


class CustomerAccount(Document):
    """
    Implementation of the Class CustomerAccount
    Created on:      19-Dec-2023 3:28:10 PM
    """

    def __init__(self):
        """
        Constructor for CustomerAccount class.
        """
        super().__init__()
        self.billing_cycle = ""
        self.budget_bill = ""
        self.last_bill_amount = Money()
        self.erp_invoices = ErpInvoice()
        self.work_billing_infos = WorkBillingInfo()
        self.payment_transactions = Transaction()
        self.account_notification = AccountNotification()
        self.customer_agreements = CustomerAgreement()
