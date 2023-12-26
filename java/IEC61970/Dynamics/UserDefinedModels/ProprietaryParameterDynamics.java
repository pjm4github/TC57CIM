package IEC61970.Dynamics.UserDefinedModels;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Float;
import IEC61970.Base.Domain.Integer;

/**
 * Supports definition of one or more parameters of several different datatypes
 * for use by proprietary user-defined models.  NOTE: This class does not inherit
 * from IdentifiedObject since it is not intended that a single instance of it be
 * referenced by more than one proprietary user-defined model instance.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:32:02 PM
 */
public class ProprietaryParameterDynamics {

	/**
	 * Used for boolean parameter value. If this attribute is populated,
	 * integerParameterValue and floatParameterValue will not be.
	 */
	public Boolean booleanParameterValue;
	/**
	 * Used for floating point parameter value.  If this attribute is populated,
	 * booleanParameterValue and integerParameterValue will not be.
	 */
	public Float floatParameterValue;
	/**
	 * Used for integer parameter value.  If this attribute is populated,
	 * booleanParameterValue and floatParameterValue will not be.
	 */
	public Integer integerParameterValue;
	/**
	 * Sequence number of the parameter among the set of parameters associated with
	 * the related proprietary user-defined model.
	 */
	public Integer parameterNumber;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public LoadUserDefined LoadUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public VoltageCompensatorUserDefined VoltageCompensatorUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public PFVArControllerType2UserDefined PFVArControllerType2UserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public VoltageAdjusterUserDefined VoltageAdjusterUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public PFVArControllerType1UserDefined PFVArControllerType1UserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public DiscontinuousExcitationControlUserDefined DiscontinuousExcitationControlUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public PowerSystemStabilizerUserDefined PowerSystemStabilizerUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public UnderexcitationLimiterUserDefined UnderexcitationLimiterUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public OverexcitationLimiterUserDefined OverexcitationLimiterUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public ExcitationSystemUserDefined ExcitationSystemUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public MechanicalLoadUserDefined MechanicalLoadUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public TurbineLoadControllerUserDefined TurbineLoadControllerUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public TurbineGovernorUserDefined TurbineGovernorUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public AsynchronousMachineUserDefined AsynchronousMachineUserDefined;
	/**
	 * Proprietary user-defined model with which this parameter is associated.
	 */
	public SynchronousMachineUserDefined SynchronousMachineUserDefined;

	public ProprietaryParameterDynamics(){

	}
}//end ProprietaryParameterDynamics