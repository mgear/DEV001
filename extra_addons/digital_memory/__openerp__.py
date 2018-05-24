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
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/digital_memory.xml',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],

    'installable': True,
    'auto_install': False,

}