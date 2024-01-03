package IEC61970.Base.Generation.GenerationTrainingSimulation;

import IEC61970.Base.Domain.Temperature;
import IEC61970.Base.Domain.PU;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Seconds;
import IEC61970.Base.Generation.Production.AirCompressor;

/**
 * A prime mover that is typically fueled by gas or light oil.
 * @created 02-Jan-2024 11:05:05 PM
 */
public class CombustionTurbine extends PrimeMover {

	/**
	 * Default ambient temperature to be used in modeling applications.
	 */
	public Temperature ambientTemp;
	/**
	 * Off-nominal frequency effect on turbine auxiliaries. Per unit reduction in
	 * auxiliary active power consumption versus per unit reduction in frequency (from
	 * rated frequency).
	 */
	public PU auxPowerVersusFrequency;
	/**
	 * Off-nominal voltage effect on turbine auxiliaries. Per unit reduction in
	 * auxiliary active power consumption versus per unit reduction in auxiliary bus
	 * voltage (from a specified voltage level).
	 */
	public PU auxPowerVersusVoltage;
	/**
	 * Off-nominal frequency effect on turbine capability. Per unit reduction in unit
	 * active power capability versus per unit reduction in frequency (from rated
	 * frequency).
	 */
	public PU capabilityVersusFrequency;
	/**
	 * Flag that is set to true if the combustion turbine is associated with a heat
	 * recovery boiler.
	 */
	public Boolean heatRecoveryFlag;
	/**
	 * Per unit change in power per (versus) unit change in ambient temperature.
	 */
	public PU powerVariationByTemp;
	/**
	 * Reference temperature at which the output of the turbine was defined.
	 */
	public Temperature referenceTemp;
	/**
	 * The time constant for the turbine.
	 */
	public Seconds timeConstant;
	/**
	 * A CAES air compressor is driven by combustion turbine.
	 */
	public AirCompressor AirCompressor;
	/**
	 * A combustion turbine may have an active power versus ambient temperature
	 * relationship.
	 */
	public CTTempActivePowerCurve CTTempActivePowerCurve;

	public CombustionTurbine(){

	}
}//end CombustionTurbine