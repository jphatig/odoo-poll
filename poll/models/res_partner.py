# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Partner(models.Model):
    """Defines citizen data"""

    _inherit = 'res.partner'

    document_type = fields.Selection(
        string='Identification Document Type',
        selection=[
            ('personal', 'Personal Identification'),
            ('passport', 'Passport'),
            ('other', 'Other')
        ],
    )
    document = fields.Char(
        string='Identification Document'
    )
    birth_date = fields.Date(
        string='Birth Date'
    )
    age = fields.Integer(
        string='Age'
    )
    sex = fields.Selection(
        string='Sex',
        selection=[
            ('male', 'Male'),
            ('female', 'Female')
        ]
    )
    gender = fields.Many2one(
        comodel_name='res.partner.gender',
        string='Gender'
    )
    residence_geounit_id = fields.Many2one(
        comodel_name='poll.geounit',
        string='Specific Residence Location'
    )
    redicende_hierarchy = fields.Char(
        string='Complete Residence Location',
        related='residence_geounit_id.hierarchy'
    )
