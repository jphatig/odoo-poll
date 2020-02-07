# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Event(models.Model):
    """Defines poll events"""

    _name = 'poll.event'

    name = fields.Char(
        string='Name',
        required=True
    )
    start_date = fields.Date(
        string='Start Date',
        readonly=True
    )
    finish_date = fields.Date(
        string='Finish Date',
        readonly=True
    )
    stand_capacity = fields.Integer(
        string='Partners per stand'
    )
    state = fields.Selection(
        string='State',
        default='new',
        selection=[
            ('new', 'New'),
            ('doing', 'Doing'),
            ('done', 'Done'),
            ('finished', 'Finished'),
            ('canceled', 'Canceled')
        ]
    )
    poll_ids = fields.One2many(
        string='Polls',
        comodel_name='poll.poll',
        inverse_name='event_id',
        readonly=False
    )

    def set_done(self):
        self.state = 'done'

    def set_finish_date(self):
        self.finish_date = fields.Datetime.now()
