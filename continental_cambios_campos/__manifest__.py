# -*- coding: utf-8 -*-
{
    'name': "Modificación de campos, taller mécanico",
    'description': """
       Modificación de campos en diferentes módulos de flota y car repair.
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': [
                'base',
                'fleet',
                'car_repair_industry',
                
                ],
    'data': [
        'views/vista_lista.xml',
        'views/vista_lista_diagnostico.xml',
        'views/vista_orden_trabajo.xml',
       # 'views/atani_add_modelo.xml',

        ],
    'installable':True,
    'auto_install':False,
}
