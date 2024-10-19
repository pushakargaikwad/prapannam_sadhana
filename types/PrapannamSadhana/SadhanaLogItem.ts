
export interface SadhanaLogItem{
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
	/**	Sadhana Type : Link - Sadhana Type	*/
	sadhana_type: string
	/**	Points : Float	*/
	rating?: number
	/**	Qty : Float	*/
	qty: number
}