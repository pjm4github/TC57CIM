from CIM_STD_PYTHON.TC57CIM.IEC61968.Customers.TroubleTicket import TroubleTicket
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


###########################################################
#  CustomerNotification.py
#  Implementation of the Class CustomerNotification
#  Created on:      19-Dec-2023 3:17:08 PM
#  Original author: T. Kostic
###########################################################


class CustomerNotification:

    def __init__(self):
        """
        Constructor for CustomerNotification class.
        """
        self.contactType = ""
        self.contactValue = ""
        self.earliestDateTimeToCall = DateTime()
        self.latestDateTimeToCall = DateTime()
        self.trigger = NotificationTriggerKind()
        self.customer = Customer()
        self.troubleTickets = TroubleTicket()
