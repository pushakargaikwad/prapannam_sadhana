import { SadhanaGroupMember } from './SadhanaGroupMember'

export interface SadhanaGroup{
	name: string
	creation: string
	modified: string
	owner: string
	modified_by: string
	docstatus: 0 | 1 | 2
	parent?: string
	parentfield?: string
	parenttype?: string
	idx?: number
	/**	Manager : Link - User	*/
	manager?: string
	/**	members : Table - Sadhana Group Member	*/
	members?: SadhanaGroupMember[]
}