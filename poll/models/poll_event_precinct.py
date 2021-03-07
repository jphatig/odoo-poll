# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class EventPrecinct(models.Model):
    """Defines poll precincts by each event"""

    _name = 'poll.event.precint'

    name = fields.Char(
        string='Name'
    )
    event_id = fields.Many2one(
        comodel_name='poll.event',
        string='Event'
    )
    precinct_id = fields.Many2one(
        comodel_name='poll.precinct',
        string='Precinct'
    )
    stand_ids = fields.One2many(
        comodel_name='poll.stand',
        inverse_name='precinct_id',
        string='Stands for voting'
    )
    active = fields.Boolean(
        string='Active',
        default=True
    )
