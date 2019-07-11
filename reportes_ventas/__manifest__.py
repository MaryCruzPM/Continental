# -*- coding: utf-8 -*-
{
    'name': "add fields en reporte de venta y factura",

    'summary': """add_fields_in report
    """,

    'description': """
        Modulo para ventas agregar en reporte los campos para el taller mecanico como: vehiculo, numero de unidad, matricula, marca, modelo.
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
        'sale_management',
        'sale',
        

        ],

	'data': [
   'views/report_ventas.xml',
   'views/reporte_factura.xml',

    ],
	'demo':[

	],
    'installable':True,
}
