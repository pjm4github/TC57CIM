package IEC61970.Base.Wires;


/**
 * Describes a symmetrical phase shifting transformer tap model in which the
 * secondary side voltage magnitude is the same as at the primary side. The
 * difference voltage magnitude is the base in an equal-sided triangle where the
 * sides corresponds to the primary and secondary voltages. The phase angle
 * difference corresponds to the top angle and can be expressed as twice the
 * arctangent of half the total difference voltage.
 * @author SELAOST1
 * @version 1.0
 * @created 25-Dec-2023 8:32:01 PM
 */
public class PhaseTapChangerSymmetrical extends PhaseTapChangerNonLinear {

	public PhaseTapChangerSymmetrical(){

	}
}//end PhaseTapChangerSymmetrical