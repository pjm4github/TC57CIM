package IEC61970.Base.Wires;

import IEC61970.Base.Domain.PerCent;
import IEC61970.Base.Domain.Integer;
import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Domain.Voltage;
import IEC61970.Base.Domain.Resistance;
import IEC61970.Base.Domain.Reactance;
import IEC61970.Base.Core.BaseVoltage;
import IEC61970.Base.Core.Terminal;
import IEC61970.Base.Core.IdentifiedObject;

/**
 * A conducting connection point of a power transformer. It corresponds to a
 * physical transformer winding terminal.  In earlier CIM versions, the
 * TransformerWinding class served a similar purpose, but this class is more
 * flexible because it associates to terminal but is not a specialization of
 * ConductingEquipment.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:32:04 PM
 */
public class TransformerEnd extends IdentifiedObject {

	/**
	 * Core shunt magnetizing susceptance in the saturation region.
	 */
	public PerCent bmagSat;
	/**
	 * Number for this transformer end, corresponding to the end's order in the power
	 * transformer vector group or phase angle clock number.  Highest voltage winding
	 * should be 1.  Each end within a power transformer should have a unique
	 * subsequent end number.   Note the transformer end number need not match the
	 * terminal sequence number.
	 */
	public Integer endNumber;
	/**
	 * (for Yn and Zn connections) True if the neutral is solidly grounded.
	 */
	public Boolean grounded;
	/**
	 * The reference voltage at which the magnetizing saturation measurements were made
	 */
	public Voltage magBaseU;
	/**
	 * Core magnetizing saturation curve knee flux level.
	 */
	public PerCent magSatFlux;
	/**
	 * (for Yn and Zn connections) Resistance part of neutral impedance where
	 * 'grounded' is true.
	 */
	public Resistance rground;
	/**
	 * (for Yn and Zn connections) Reactive part of neutral impedance where 'grounded'
	 * is true.
	 */
	public Reactance xground;
	/**
	 * Phase tap changer associated with this transformer end.
	 */
	public PhaseTapChanger PhaseTapChanger;
	/**
	 * (accurate for 2- or 3-winding transformers only) Pi-model impedances of this
	 * transformer end. By convention, for a two winding transformer, the full values
	 * of the transformer should be entered on the high voltage end (endNumber=1).
	 */
	public TransformerStarImpedance StarImpedance;
	/**
	 * Ratio tap changer associated with this transformer end.
	 */
	public RatioTapChanger RatioTapChanger;
	/**
	 * Base voltage of the transformer end.  This is essential for PU calculation.
	 */
	public BaseVoltage BaseVoltage;
	/**
	 * Terminal of the power transformer to which this transformer end belongs.
	 */
	public Terminal Terminal;

	public TransformerEnd(){

	}
}//end TransformerEnd