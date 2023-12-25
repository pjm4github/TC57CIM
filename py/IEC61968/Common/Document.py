from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ConfigurationEvent import ConfigurationEvent
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ElectronicAddress import ElectronicAddress
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class Document(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.author_name = ""
        self.comment = ""
        self.created_date_time = DateTime()
        self.doc_status = Status()
        self.electronic_address = ElectronicAddress()
        self.last_modified_date_time = DateTime()
        self.revision_number = ""
        self.status = Status()
        self.subject = ""
        self.title = ""
        self.type = ""
        self.configuration_events = ConfigurationEvent()
