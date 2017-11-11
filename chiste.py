# -*- coding: utf-8 -*-
from osv import osv, fields


class categoria(osv.osv): 
	_name = 'chiste.categoria'
	_columns = {
		'name' : fields.char('Name', size=64, select=1),
		'description' : fields.char('Description', size=64),
		
	}





class chiste(osv.osv): 
	_name = 'chiste.chiste'
	_columns = {
		'title' : fields.char('Title', size=64, select=1),
		'description' : fields.text('Description'),
		'category_id': fields.many2one('chiste.categoria','Category')
	}
chiste()

class chiste2(osv.osv):
	_name = 'chiste.chiste'
	_inherit = 'chiste.chiste'

chiste2()