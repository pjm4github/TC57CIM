from IEC61968.Customers.Customer import Customer
from IEC61968.Customers.NotificationTriggerKind import NotificationTriggerKind
from IEC61968.Customers.TroubleTicket import TroubleTicket
from IEC61970.Base.Domain.DateTime import DateTime


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
        self.trigger = NotificationTriggerKind.INITIAL_ETR
        self.customer = Customer()
        self.troubleTickets = TroubleTicket()
