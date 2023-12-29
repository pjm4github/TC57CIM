# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
class SchedulingCoordinatorUser:
    """
    Describing users of a Scheduling Coordinator.
    @created 28-Dec-2023 12:23:13 PM
    """

    def __init__(self) -> None:
        self.login_id: str = ""  # Login ID
        self.login_role: str = ""  # Assigned roles (these are roles with either Read or Read/Write privileges on different Market Systems)
