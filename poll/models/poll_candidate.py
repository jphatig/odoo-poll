# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Candidate(models.Model):
    """Defines partner as candidates"""

    _name = 'poll.candidate'

    partner_id = fields.Many2one(
        comodel='res.partner',
        string='Partner'
    )
    name = fields.Char(
        string='Name',
        related='partner_id.name'
    )
    political_party = fields.Many2one(
        comodel_name='poll.political.party',
        string='Political Party'
    )
