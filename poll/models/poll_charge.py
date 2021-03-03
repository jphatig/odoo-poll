# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Charge(models.Model):
    """Defines charges which ones a canditate could be elected"""

    _name = 'poll.charge'

    name = fields.Char(
        string='Name'
    )
    geounit_type_id = fields.Many2one(
        comodel_name='poll.geounit.type',
        string='Geolocation type jurisdiction'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
