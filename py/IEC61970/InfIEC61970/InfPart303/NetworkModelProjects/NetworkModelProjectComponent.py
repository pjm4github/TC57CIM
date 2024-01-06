
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.CurrentState import CurrentState
from IEC61970.InfIEC61970.InfPart303.NetworkModelProjects.NetworkModelProject2 import NetworkModelProject2


# package IEC61970.InfIEC61970.InfPart303.NetworkModelProjects;
#
# import IEC61970.Base.Core.IdentifiedObject;
#
# /**
#  * Abstract class for both a network model project and network model change.
#  * @author 222206
#  * @version 1.0
#  * @created 25-Dec-2023 8:32:00 PM
#  */
# public class NetworkModelProjectComponentP extends IdentifiedObject {
#
# 	public NetworkModelProjectDocument m_NetworkModelProjectDocument;
# 	/**
# 	 * The parent project of this project.
# 	 */
# 	public NetworkModelProject ContainingProject;
#
# 	public NetworkModelProjectComponent(){
#
# 	}
# }//end NetworkModelProjectComponent
#

class NetworkModelProjectComponent(IdentifiedObject):
    """
    Author: SELAOST1
    Version: 1.0
    Created: 25-Dec-2023 8:32:00 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.closed = DateTime()  # Date/time when the project component was closed
        self.created = DateTime()  # Creation date/time of the project component
        self.updated = DateTime()  # Date/time when the project component was last updated
        self.version = int()  # Version of the project component
        self.current_state = CurrentState()  # Placeholder for associated CurrentState
        self.parent = NetworkModelProject2()  # Placeholder for the parent project (NetworkModelProject2)
