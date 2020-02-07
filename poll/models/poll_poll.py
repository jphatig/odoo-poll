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
        """Set poll as doing """
        self.check_doing_new()
        self.check_doing_unique()
        self.set_doing()
        self.set_doing_start_date()

    def set_doing(self):
        self.state = self.event_id.state = 'doing'

    def set_doing_start_date(self):
        self.start_date = self.event_id.start_date = fields.Datetime.now()

    def check_doing_new(self):
        if self.state not in ['new']:
            raise exceptions.ValidationError(
                'Only new polls can be marked as doing'
            )

    def check_doing_unique(self):
        if self.event_id.poll_ids.filtered(lambda x: x.state in ['doing']):
            raise exceptions.ValidationError(
                'It cannot be more than one poll doing per event'
            )

    def state_done(self):
        self.check_done_doing()
        self.set_done()
        self.set_done_finish_date()


    def check_done_doing(self):
        if self.state not in ['doing']:
            raise exceptions.ValidationError(
                'Only doing polls can be marked as done'
            )

    def set_done(self):
        self.state = 'done'

    def set_done_finish_date(self):
        self.finish_date = fields.Datetime.now()

    def set_relatives_done(self):
        if not self.event_id.poll_ids.filtered(lambda x: x.state in ['new']):
            self.event_id.set_done()
            self.event_id.set_finish_date()
