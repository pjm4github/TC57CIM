# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from datetime import datetime
from typing import Optional

class Capability:

    def __init__(self) -> None:
        self.performance_factorOptional[str] = None  # Capability performance factor
        self.statusOptional[Status] = None
        self.typeOptional[str] = None  # Classification by utility's work management standards and practices
        self.validity_intervalOptional[DateTimeInterval] = None  # Date and time interval for which this capability is valid (when it became effective and when it expires)
        self.work_tasksOptional[OldWorkTask] = None
        self.crewOptional[OldCrew] = None
        self.craftsOptional[Craft] = None

class WorkIdentifiedObject:
    pass

class Status:
    pass

class DateTimeInterval:
    pass

class OldWorkTask:
    pass

class OldCrew:
    pass

class Craft:
    pass
