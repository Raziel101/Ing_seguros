# -*- coding: utf-8 -*-
{
    'name': "Administración de Seguros ",

    'summary': """
        Administración de Seguros del Personal""",

    'description': """
        Administración de Seguros del Personal
    """,

    'author': "Ingenio Solutions",
    'website': "http://www.ingeniosolutions.com.ar",
    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', "mail", 'ing_ausencias'],
    'data': [
        # Security
        'security/ir.model.access.csv',
        'security/security.xml',

        # Menu
        'menu_view.xml',

        # Views
        'views/ing_secure_view.xml',
        'views/hr_employee_view.xml',
        'views/config.xml',
        'views/planilla_art.xml',
        'views/plantilla_iasper.xml',

        #REPORTS
        'reports/report_planilla_art.xml',

        # WIZARD
        'wizard/alta_baja_seguros.xml',

    ],
}
