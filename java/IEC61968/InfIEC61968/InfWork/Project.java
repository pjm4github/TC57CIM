package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.Money;

/**
 * A collection of related work. For construction projects and maintenance
 * projects, multiple phases may be performed.
 * @created 03-Jan-2024 12:59:20 PM
 */
public class Project extends WorkDocument {

	/**
	 * Overall project budget.
	 */
	public Money budget;
	public Project SubProjects;

	public Project(){

	}
}//end Project