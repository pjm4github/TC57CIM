# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from IEC61968.Common.Document import Document
from IEC61968.Customers.CustomerAccount import CustomerAccount
from IEC61968.InfIEC61968.InfCustomers.CustomerBillingKind import CustomerBillingKind
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoiceLineItem import ErpInvoiceLineItem
from IEC61968.InfIEC61968.InfWork.NonStandardItem import Money
from IEC61970.Base.Domain.Date import Date


class CustomerBillingInfo(Document):
    def __init__(self):
        super().__init__()
        self.billing_date = Date()  # Business date designated for the billing run
        self.due_date = Date()  # Calculated date upon which a customer billing amount is due
        self.kind = CustomerBillingKind.CONSOLIDATED_ESS  # Kind of bill customer receives
        self.last_payment_amt = Money(0)  # Amount of the last payment received from the customer
        self.last_payment_date = Date()  # Date of the last payment received from the customer
        self.out_balance = Money(0)  # Outstanding balance on the CustomerAccount
        self.pymt_plan_amt = Money(0)  # Monthly amortized amount due during each billing cycle
        self.pymt_plan_type = ""  # Type of payment plan
        self.erp_invoice_line_items = ErpInvoiceLineItem()
        self.customer_account = CustomerAccount()
