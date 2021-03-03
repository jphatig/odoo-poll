# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class PoliticalParty(models.Model):
    """Defines political parties"""

    _name = 'poll.political.party'

    name = fields.Char(
        string='Name'
    )
    logo = fields.Binary(
        string='logo'
    )
    code = fields.Char(
        string='Code'
    )
    description = fields.Text(
        string='Description'
    )
    state = fields.Selection(
        string='Political State',
        default='enabled',
        selection=[
            ('enabled', 'Enabled'),
            ('disabled', 'Disabled')
        ]
    )
    legal_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Legal partner'
    )
    candidate_ids = fields.One2many(
        comodel_name='poll.candidate',
        inverse_name='political_party_id',
        string='Candidates',
        readonly=False
    )
    goverment_plan = fields.Binary(
        string='Goverment plan'
    )
    goverment_plan_filename = fields.Char(
        string='Goverment plan filename',
        compute='_goverment_plan_filename'
    )
    active = fields.Boolean(
        string='active',
        default=True
    )

    def _underlined_name(self):
        return self.name.lower().replace(' ', '_') if self.name else 'unmamed'

    def _goverment_plan_filename(self):
        for record in self:
            record.goverment_plan_filename = 'goverment_plan_' + record._underlined_name() + '.pdf'
