package IEC61968.AssetInfo;

import IEC61970.Base.Domain.Capacitance;
import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.CurrentFlow;
import IEC61970.Base.Domain.Voltage;
import IEC61968.Assets.AssetInfo;

/**
 * Bushing datasheet information.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:19 PM
 */
public class BushingInfo extends AssetInfo {

	/**
	 * Factory measured capacitance, measured between the power factor tap and the
	 * bushing conductor.
	 */
	public Capacitance c1Capacitance;
	/**
	 * Factory measured insulation power factor, measured between the power factor tap
	 * and the bushing conductor.
	 */
	public PerCent c1PowerFactor;
	/**
	 * Factory measured capacitance measured between the power factor tap and ground.
	 */
	public Capacitance c2Capacitance;
	/**
	 * Factory measured insulation power factor, measured between the power factor tap
	 * and ground.
	 */
	public PerCent c2PowerFactor;
	/**
	 * Kind of insulation.
	 */
	public BushingInsulationKind insulationKind;
	/**
	 * Rated current for bushing as installed.
	 */
	public CurrentFlow ratedCurrent;
	/**
	 * Rated impulse withstand voltage, also known as BIL (Basic Impulse Level).
	 */
	public Voltage ratedImpulseWithstandVoltage;
	/**
	 * Rated line-to-ground voltage. Also referred to as U<sub>y</sub> on bushing
	 * nameplate.
	 */
	public Voltage ratedLineToGroundVoltage;
	/**
	 * Rated voltage. Can be referred to as U<sub>m</sub>, system voltage or class on
	 * bushing nameplate.
	 */
	public Voltage ratedVoltage;

	public BushingInfo(){

	}
}//end BushingInfo