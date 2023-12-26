package IEC61968.Metering;


/**
 * Reason for the reading being taken.
 * @author T. Kostic
 * @version 1.0
 * @created 25-Dec-2023 8:45:24 PM
 */
public enum ReadingReasonKind {
	/**
	 * Reading(s) taken or to be taken in conjunction with installation of a meter.
	 */
	installation,
	/**
	 * Reading(s) taken or to be taken in conjunction with removal of a meter.
	 */
	removal,
	/**
	 * Reading(s) taken or to be taken in response to an inquiry by a customer or
	 * other party.
	 */
	inquiry,
	/**
	 * Reading(s) taken or to be taken in response to a billing-related inquiry by a
	 * customer or other party. A variant of 'inquiry'.
	 */
	billing,
	/**
	 * Reading(s) taken or to be taken in conjunction with a customer move-in event.
	 */
	moveIn,
	/**
	 * Reading(s) taken or to be taken in conjunction with a customer move-out event.
	 */
	moveOut,
	/**
	 * Reading(s) taken or to be taken in conjunction with the resetting of one or
	 * more demand registers in a meter.
	 */
	demandReset,
	/**
	 * Reading(s) taken or to be taken in conjunction with a disconnection of service.
	 */
	serviceDisconnect,
	/**
	 * Reading(s) taken or to be taken in conjunction with a connection or re-
	 * connection of service.
	 */
	serviceConnect,
	/**
	 * Reading(s) taken or to be taken to support management of loads on distribution
	 * networks or devices.
	 */
	loadManagement,
	/**
	 * Reading(s) taken or to be taken to support research and analysis of loads on
	 * distribution networks or devices.
	 */
	loadResearch,
	/**
	 * Reading(s) taken or to be taken for some other reason or purpose.
	 */
	other
}