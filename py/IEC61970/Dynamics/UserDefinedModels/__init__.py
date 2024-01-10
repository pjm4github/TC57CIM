__description__ = """
This section contains user-defined dynamic model classes to support the exchange of both proprietary and explicitly 
defined user-defined models.  

Proprietary models represent behaviour which, while not defined by a standard model class, is mutually understood by 
the sending and receiving applications based on the name passed in the .name attribute of the appropriate 
xxxUserDefined class.  Proprietary model parameters are passed as general attributes using as many instances of 
the ProprietaryParameterDynamics class as there are parameters.

Explicitly defined models describe dynamic behaviour in detail in terms of control blocks and their input and output 
signals.  NOTE: The classes to support explicitly defined modelling are not currently defined - it is future work 
intended to also be supported by the family of xxxUserDefined classes.

Both types of user-defined models use the family of xxxUserDefined classes, which allow a user-defined model 
to be utilized:
as the model for an individual standard function block (like turbine-governor or power system stabilizer) in a 
standard interconnection model whose other function blocks could be either standard or user-defined.  For an 
illustration of this form of usage for a proprietary model, see the ExampleFunctionBlockProprietaryModel diagram 
in the Examples section.
as the complete representation of a dynamic behaviour model (for an entire synchronous machine, for example) where 
standard function blocks and standard interconnections are not used at all. For an illustration of this form of 
usage for a proprietary model, see the ExampleCompleteProprietaryModel diagram in the Examples section.
"""