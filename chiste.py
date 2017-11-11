# -*- coding: utf-8 -*-
from osv import osv, fields

class chiste(osv.osv): 
	_name = 'chiste.chiste'
	_columns = {
		'title' : fields.char('Title', size=64, select=1),
		'description' : fields.text('Description')

	}
chiste()

class chiste2(osv.osv):
	_name = 'chiste.chiste'
	_inherit = 'chiste.chiste'

chiste2()