package IEC61970.Part552Header.ModelDescription;


/**
 * @author selaost1
 * @version 1.0
 * @created 25-Dec-2023 8:32:00 PM
 */
public class Model {

	public DateTime created;
	public String description;
	public URI modelingAuthoritySet;
	public URI profile;
	public DateTime scenarioTime;
	public Integer version;
	public Model Supersedes;
	public Model DependentOn;

	public Model(){

	}
}//end Model