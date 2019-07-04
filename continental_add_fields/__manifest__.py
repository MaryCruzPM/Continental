# -*- coding: utf-8 -*-
{
    'name': "Add fields a flota",

    'summary': """add fields
    """,

    'description': """
        Modulo para agregar campos al modulo de flota
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
        'fleet'
        ],

	'data': [
               'views/fields_flota.xml',
    
    ],
	'demo':[

	],
    'installable':True,
}
