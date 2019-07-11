# -*- coding: utf-8 -*-
{
    'name': "continental_mecanico",

    'summary': """
        Cambiar el tipo mecanico <res.user> a <res.partner>
        """,

    'description': """
        Cambiar el tipo mecanico <res.user> a <res.partner>
    """,

    'author': "Soluciones 4G",
    'website': "soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    'car_repair_industry',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/etiquetas.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}