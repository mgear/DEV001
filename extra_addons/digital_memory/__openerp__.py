# -*- coding: utf-8 -*-
{
    'name': "Digital Memory",

    'summary': """Manage digital memory""",

    'description': """
        Digital Memory module for managing wiki:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Khlon Yuriy",
    'maintainer': 'Simbioz Holding',
    'website': "http://www.simbioz.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
        'views/digital_memory',
    ],

    'installable': True,
    'auto_install': False,

}