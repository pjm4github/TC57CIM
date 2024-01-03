package IEC61970.InfIEC61970.InfSIPS;

import IEC61970.Base.Domain.Boolean;
import IEC61970.Base.Core.PowerSystemResource;

/**
 * Remedial Action Scheme (RAS), Special Protection Schemes (SPS), System
 * Protection Schemes (SPS) or System Integrity Protection Schemes (SIPS).
 * @author sveinols
 * @version 1.0
 * @created 02-Jan-2024 9:34:29 PM
 */
public class RemedialActionScheme extends PowerSystemResource {

	/**
	 * The status of the class set by operation or by signal. Optional field that will
	 * override other status fields.
	 */
	public Boolean armed;
	/**
	 * Kind of Remedial Action Scheme (RAS)
	 */
	public RemedialActionSchemeKind kind;
	/**
	 * The default/normal value used when other active signal/values are missing.
	 */
	public Boolean normalArmed;
	public Stage Stage;

	public RemedialActionScheme(){

	}
}//end RemedialActionScheme