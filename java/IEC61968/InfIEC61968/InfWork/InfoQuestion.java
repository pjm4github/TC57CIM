package IEC61968.InfIEC61968.InfWork;

import IEC61970.Base.Domain.String;
import IEC61970.Base.Domain.DateTime;

/**
 * Questions and answers associated with a type of document for purposes of
 * clarification. Questions may be predefined or ad hoc.
 * @created 02-Jan-2024 9:58:07 PM
 */
public class InfoQuestion extends WorkDocument {

	/**
	 * Answer to question.
	 */
	public String answer;
	/**
	 * The date and time the quesiton was answered.
	 */
	public DateTime answerDateTime;
	/**
	 * Remarks to qualify the answer.
	 */
	public String answerRemark;
	/**
	 * The question code. If blank, refer to questionText.
	 */
	public String questionCode;
	/**
	 * Remarks to qualify the question in this situation.
	 */
	public String questionRemark;
	/**
	 * For non-coded questions, the question is provided here.
	 */
	public String questionText;
	/**
	 * The type of the question.
	 */
	public String questionType;

	public InfoQuestion(){

	}
}//end InfoQuestion