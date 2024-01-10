from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.Wires.SynchronousMachine import SynchronousMachine


class PrimeMover(PowerSystemResource):
    """
    The machine used to develop mechanical energy used to drive a generator.
    Created: 02-Jan-2024 11:06:18 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.prime_mover_rating = 0.0  # Rating of prime mover
        self.synchronous_machines = SynchronousMachine()  # Synchronous machines this Prime mover drives
        # Assuming PowerSystemResource, Float, and SynchronousMachine are previously defined classes
        # If they are not defined, these will raise an error and need to be implemented
