###########################################################
#  Customer.py
#  Implementation of the Class Customer
#  Created on:      19-Dec-2023 3:27:42 PM
###########################################################
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.OrganisationRole import OrganisationRole
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Priority import Priority
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.CustomerKind import CustomerKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.OutagePlan import OutagePlan


class Customer(OrganisationRole):

    def __init__(self):
        """
        Constructor for Customer class.
        """
        super().__init__()
        self.kind = CustomerKind.RESIDENTIAL
        self.locale = ""
        self.priority = Priority()
        self.puc_number = ""
        self.special_need = ""
        self.status = Status()
        self.vip = False
        self.end_devices = [EndDevice()]
        self.customer = Customer()
        self.customer_accounts = [CustomerAccount()]
        self.erp_persons = [OldPerson()]
        self.customer_agreements = [CustomerAgreement()]
        self.works = [Work()]
        self.outage_plan = OutagePlan()
