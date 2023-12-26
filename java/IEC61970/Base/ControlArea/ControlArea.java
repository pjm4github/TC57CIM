package IEC61970.Base.ControlArea;

import IEC61970.Base.Domain.ActivePower;
import IEC61970.Base.LoadModel.EnergyArea;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * A control area is a grouping of generating units and/or loads and a cutset of
 * tie lines (as terminals) which may be used for a variety of purposes including
 * automatic generation control, powerflow solution area interchange control
 * specification, and input to load forecasting.   Note that any number of
 * overlapping control area specifications can be superimposed on the physical
 * model.
 * @author kdd
 * @version 1.0
 * @created 25-Dec-2023 8:31:55 PM
 */
public class ControlArea extends PowerSystemResource {

	/**
	 * The specified positive net interchange into the control area, i.e. positive
	 * sign means flow in to the area.
	 */
	public ActivePower netInterchange;
	/**
	 * Active power net interchange tolerance
	 */
	public ActivePower pTolerance;
	/**
	 * The primary type of control area definition used to determine if this is used
	 * for automatic generation control, for planning interchange control, or other
	 * purposes.   A control area specified with primary type of automatic generation
	 * control could still be forecast and used as an interchange area in power flow
	 * analysis.
	 */
	public ControlAreaTypeKind type;
	/**
	 * The energy area that is forecast from this control area specification.
	 */
	public EnergyArea EnergyArea;
	/**
	 * The generating unit specificaitons for the control area.
	 */
	public ControlAreaGeneratingUnit ControlAreaGeneratingUnit;
	/**
	 * The tie flows associated with the control area.
	 */
	public TieFlow TieFlow;

	public ControlArea(){

	}
}//end ControlArea