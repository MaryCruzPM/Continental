# -*- coding: utf-8 -*-
{
    'name': "sale_order campos default de vehiculo",

    'summary': """editable y default
    """,

    'description': """
        Modulo para default en ventas paa taller mecanico
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts',
        'sale'
        ],

 

    # always loaded
	'data': [
               'views/sale_order.xml',
               'views/account_invoice_add.xml',
    
    ],
	'demo':[

	],
    'installable':True,
}
