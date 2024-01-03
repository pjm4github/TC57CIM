package IEC61970.Base.Equivalents;

import IEC61970.Base.Domain.Susceptance;
import IEC61970.Base.Domain.Conductance;

/**
 * The class represents equivalent shunts.
 * @created 02-Jan-2024 10:46:46 PM
 */
public class EquivalentShunt extends EquivalentEquipment {

	/**
	 * Positive sequence shunt susceptance.
	 */
	public Susceptance b;
	/**
	 * Positive sequence shunt conductance.
	 */
	public Conductance g;

	public EquivalentShunt(){

	}
}//end EquivalentShunt