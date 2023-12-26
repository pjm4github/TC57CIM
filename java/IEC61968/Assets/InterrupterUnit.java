package IEC61968.Assets;


/**
 * Breaker interrupter.
 * Some interrupters have one fixed and one moving contact, some have 2 fixed
 * contacts, some 2 moving contacts. An interrupter will have relationships with 2
 * bushings and those relationships may be any combination of the FixedContact and
 * MovingContact associations.
 * @author ppbr003
 * @version 1.0
 * @created 25-Dec-2023 8:45:22 PM
 */
public class InterrupterUnit extends Asset {

	/**
	 * Bushing(s) to which the fixed contact(s) of this interrupter is(are) attached.
	 * Some interrupters have one fixed and one moving contact, some have 2 fixed
	 * contacts, some 2 moving contacts. An interrupter will have relationships with 2
	 * bushings and those relationships may be any combination of the FixedContact and
	 * MovingContact associations.
	 */
	public Bushing Bushing;

	public InterrupterUnit(){

	}
}//end InterrupterUnit