package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.DateTimeInterval;

/**
 * An assignment is given to an ErpPerson, Crew, Organisation, Equipment Item,
 * Tool, etc. and may be used to perform Work, WorkTasks, Procedures, etc.
 * TimeSchedules may be set up directly for Assignments or indirectly via the
 * associated WorkTask. Note that these associations are all inherited through the
 * recursive relationship on Document.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class Assignment extends WorkDocument {

	/**
	 * Period between the assignment becoming effective and its expiration.
	 */
	public DateTimeInterval effectivePeriod;

	public Assignment(){

	}
}//end Assignment