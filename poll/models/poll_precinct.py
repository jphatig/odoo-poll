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
        string='Geounit Type'
    )
    geounit_id = fields.Many2one(
        comodel_name='poll.geounit',
        string='Geounit'
    )
    address = fields.Char(
        string='Address'
    )
    stand_ids = fields.One2many(
        comodel_name='poll.stand',
        inverse_name='precinct_id',
        string='Stands'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )

    def generate_stands(self):
        pass
