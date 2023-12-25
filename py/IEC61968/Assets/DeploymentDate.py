# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime

class DeploymentDate:
    
    def __init__(self):
        self.in_service_date = DateTime()
        self.installed_date = DateTime()
        self.not_yet_installed_date = DateTime()
        self.out_of_service_date = DateTime()
        self.removed_date = DateTime()
