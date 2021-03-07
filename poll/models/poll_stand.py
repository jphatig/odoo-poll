# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Stand(models.Model):
    """Defines poll stands used by people for voting"""

    _name = 'poll.stand'

    name = fields.Char(
        string='Description'
    )
    precinct_id = fields.Many2one(
        comodel_name='poll.precinct',
        string='Precinct'
    )
    person_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='stand_id'
    )
    gender_id = fields.Many2one(
        comodel_name='res.partner.gender',
        string='Gender'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
