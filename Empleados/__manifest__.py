# -*- coding: utf-8 -*-
{
    'name': 'Empleados',
    'version': '1.0',
    'category': 'Trabajadores',
    'summary': 'Created by Leandro and Kevin',
    'description': '''
        This module was created by Leandro and Kevin.
        Features include:
        - Custom models and views
        - Basic CRUD operations
        - User-friendly interface
    ''',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/trabajadores_views.xml',
        'views/Empleado_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
