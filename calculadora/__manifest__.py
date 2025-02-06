# -*- coding: utf-8 -*-
{
    'name': 'Calculadora de Retenciones',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Calcula retenciones de empleados',
    'description': '''
        Módulo para calcular retenciones de la Seguridad Social de los empleados.
    ''',
    'depends': ['base', 'Empleados'],
    'data': [
        'security/ir.model.access.csv',
        'views/calculo_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
} 