from IEC61970.Base.Domain.Reactance import Reactance
from IEC61970.Base.Domain.Resistance import Resistance
from IEC61970.Base.Equivalents.EquivalentEquipment import EquivalentEquipment


class EquivalentBranch(EquivalentEquipment):
    """
    The class represents equivalent branches.
    Created: 07-Jan-2024 9:58:56 PM
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.negative_r12 = Resistance()  # Negative sequence series resistance from terminal sequence 1 to 2, Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange
        self.negative_r21 = Resistance()  # Negative sequence series resistance from terminal sequence 2 to 1. Used for short circuit data exchange according to IEC 60909 EquivalentBranch is a result of network reduction prior to the data exchange
        self.negative_x12 = Reactance()   # Negative sequence series reactance from terminal sequence 1 to 2. Used for short circuit data exchange according to IEC 60909, Usage : EquivalentBranch is a result of network reduction prior to the data exchange
        self.negative_x21 = Reactance()   # Negative sequence series reactance from terminal sequence 2 to 1. Used for short circuit data exchange according to IEC 60909. Usage: EquivalentBranch is a result of network reduction prior to the data exchange
        self.positive_r12 = Resistance()  # Positive sequence series resistance from terminal sequence 1 to 2. Used for short circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction prior to the data exchange.
        self.positive_r21 = Resistance()  # Positive sequence series resistance from terminal sequence 2 to 1. Used for short circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction prior to the data exchange
        self.positive_x12 = Reactance()   # Positive sequence series reactance from terminal sequence 1 to 2. Used for short circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to the data exchange
        self.positive_x21 = Reactance()   # Positive sequence series reactance from terminal sequence 2 to 1. Used for short circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to the data exchange
        self.r = Resistance()             # Positive sequence series resistance of the reduced branch.
        self.r21 = Resistance()           # Resistance from terminal sequence 2 to 1 for steady state power flow.
        self.x = Reactance()              # Positive sequence series reactance of the reduced branch.  Used for steady state power flow. This attribute is optional and represent unbalanced network such as off-nominal phase shifter. If only EquivalentBranch.r is given, then EquivalentBranch.r21 is assumed equal to EquivalentBranch.r. Usage rule : EquivalentBranch is a result of network reduction prior to the data exchange.
        self.x21 = Reactance()            # Reactance from terminal sequence 2 to 1 for steady state power flow. Used for short circuit data exchange according to IEC 60909. EquivalentBranch is a result of network reduction prior to the data exchange
        self.zero_r12 = Resistance()      # Zero sequence series resistance from terminal sequence 1 to 2. Used for short circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to the data exchange
        self.zero_r21 = Resistance()      # Zero sequence series resistance from terminal sequence 2 to 1. Used for short circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to the data exchange
        self.zero_x12 = Reactance()       # Zero sequence series reactance from terminal sequence 1 to 2. Used for short circuit data exchange according to IEC 60909. Usage : EquivalentBranch is a result of network reduction prior to the data exchange
        self.zero_x21 = Reactance()       # Zero sequence series reactance from terminal sequence 2 to 1
