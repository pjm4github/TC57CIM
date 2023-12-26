package IEC61970.Dynamics.StandardModels.PowerSystemStabilizerDynamics;


/**
 * Input signal type.  In Dynamics modelling, commonly represented by j parameter.
 * @author tsaxton
 * @version 1.0
 * @created 25-Dec-2023 8:31:59 PM
 */
public enum InputSignalKind {
	/**
	 * Input signal is rotor or shaft speed (angular frequency).
	 */
	rotorSpeed,
	/**
	 * Input signal is rotor or shaft angular frequency deviation.
	 */
	rotorAngularFrequencyDeviation,
	/**
	 * Input signal is bus voltage fr<font color="#0f0f0f">equency.  This could be a
	 * terminal frequency or remote frequency.</font>
	 */
	busFrequency,
	/**
	 * Input signal is deviation of bus voltage frequ<font color="#0f0f0f">ency.  This
	 * could be a terminal frequency deviation or remote frequency deviation.</font>
	 */
	busFrequencyDeviation,
	/**
	 * Input signal is generator electrical power on rated S.
	 */
	generatorElectricalPower,
	/**
	 * Input signal is generating accelerating power.
	 */
	generatorAcceleratingPower,
	/**
	 * Input signal <font color="#0f0f0f">is bus voltage.  This could be a terminal
	 * voltage or remote voltage.</font>
	 */
	busVoltage,
	/**
	 * Input signal is derivative of bus voltag<font color="#0f0f0f">e.  This could be
	 * a terminal voltage derivative or remote voltage derivative.</font>
	 */
	busVoltageDerivative,
	/**
	 * Input signal is amplitude of remote branch current.
	 */
	branchCurrent,
	/**
	 * Input signal is generator field current.
	 */
	fieldCurrent
}