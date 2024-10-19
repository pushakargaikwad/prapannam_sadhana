import { SadhanaLogItem } from './SadhanaLogItem'

export interface SadhanaLog{
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
	/**	Date : Date	*/
	date: string
	/**	By : Link - User	*/
	by: string
	/**	Group : Link - Sadhana Group	*/
	group: string
	/**	Total Points : Float	*/
	total_points?: number
	/**	Log Items : Table - Sadhana Log Item	*/
	log_items?: SadhanaLogItem[]
}