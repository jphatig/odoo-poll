# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Precinct(models.Model):
    """Defines poll precincts: physical location for voting"""

    _name = 'poll.precinct'

    name = fields.Char(
        string='Name'
    )
    geounit_type_id = fields.Many2one(
        comodel_name='poll.geounit.type',
        string='Geounit'
    )
    address = fields.Char(
        string='Address'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
