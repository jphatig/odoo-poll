# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Poll(models.Model):
    """Defines polls by events"""

    _name = 'poll.poll'

    name = fields.Char(
        string='Name',
        required=True
    )
    event_id = fields.Many2one(
        string='Event',
        comodel_name='poll.event',
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
    state = fields.Selection(
        string='State',
        default='new',
        selection=[
            ('new', 'New'),
            ('doing', 'Doing'),
            ('done', 'Done'),
            ('canceled', 'Canceled')
        ]
    )

    def state_doing(self):
        if self.state not in ['new']:
            raise exceptions.ValidationError(
                'Only new polls can be marked as doing'
            )
        if self.event_id.poll_ids.filtered(lambda x: x.state in ['doing']):
            raise exceptions.ValidationError(
                'It cannot be more than one poll doing per event'
            )
        self.state = self.event_id.state = 'doing'
        self.start_date = self.event_id.start_date = fields.Datetime.now()

    def state_done(self):
        if self.state not in ['doing']:
            raise exceptions.ValidationError(
                'Only doing polls can be marked as done'
            )
        self.state = 'done'
        self.finish_date = fields.Datetime.now()
        if not self.event_id.poll_ids.filtered(lambda x: x.state in ['new']):
            self.event_id.state = 'done'
            self.event_id.finish_date = fields.Datetime.now()
