# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 16:32:51 2023
from IEC61968.InfIEC61968.InfLocations.RedLine import IdentifiedObject
from IEC61970.Base.Wires.EnergyConsumer import EnergyConsumer


class LoadDynamics(IdentifiedObject):
    """
    Load whose behaviour is described by reference to a standard model or by definition of a user-defined model.

    A standard feature of dynamic load behaviour modelling is the ability to associate the same behaviour to multiple energy consumers by means of a single aggregate load definition. Aggregate loads are used to represent all or part of the real and reactive load from one or more loads in the static (power flow) data. This load is usually the aggregation of many individual load devices and the load model is approximate representation of the aggregate response of the load devices to system disturbances. The load model is always applied to individual bus loads (energy consumers) but a single set of load model parameters can be used for all loads in the grouping.
    """
    def __init__(self) -> None:
        super().__init__()
        self.energy_consumer: EnergyConsumer = EnergyConsumer()  # Energy consumer to which this dynamics load model applies
