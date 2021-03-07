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
        # Data
        'data/ir_module_category.xml',
        'data/res_groups.xml',
        'data/res_partner_gender.xml',
        # Views
        'views/poll_geounit.xml',
        'views/poll_geounit_type.xml',
        'views/poll_event.xml',
        'views/poll_poll.xml',
        'views/poll_political_party.xml',
        'views/poll_candidate.xml',
        'views/poll_charge.xml',
        'views/res_partner.xml',
        'views/poll_precinct.xml',
        # Menus
        'menus/root.xml',
        # Access Control Rules
        'security/ir.model.access.csv'
    ],
    'demo': [],
    'application': True,
    'installable': True

}
