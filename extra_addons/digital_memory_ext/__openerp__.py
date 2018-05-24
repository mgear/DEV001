# -*- coding: utf-8 -*-
{
    'name': "Digital Memory Ext",

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
    'depends': ['digital_memory', 'mail'],

    # always loaded
    'data': [
        'views/digital_memory_ext.xml'
    ],

    'installable': True,
    'auto_install': False,

}