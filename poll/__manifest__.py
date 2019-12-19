# -*- coding: utf-8 -*-
{
    'name': "Poll Management",

    'summary': """Manage electoral polls""",

    # 'description': """ ... """,

    'author': "Jhair Patiño",
    'website': "",
    'license': '',
    'category': '',
    'version': '0.0.1',

    'depends': [
        'base',
        'website'
    ],

    'data': [
        # Views
        'views/poll_geounit.xml',
        'views/poll_geounit_type.xml',
        'views/poll_event.xml',
        'views/poll_poll.xml',
        # Menus
        'menus/root.xml',
        # Access Control Rules
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'application': True,
    'installable': True

}
