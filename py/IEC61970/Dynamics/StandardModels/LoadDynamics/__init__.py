__description__ = """
Dynamic load models are used to represent the dynamic real and reactive load behaviour of a load from the static 
power flow model.  

Dynamic load models can be defined as applying either to a single load (energy consumer) or to a group of energy 
consumers.  

Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or 
asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.  
In the CIM, such individual modelling is handled by child classes of either the SynchronousMachineDynamics or 
AsynchronousMachineDynamics classes.
"""