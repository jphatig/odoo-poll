# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class PoliticalParty(models.Model):
    """Defines political parties"""

    _name = 'poll.political.party'

    name = fields.Char(
        string='Name'
    )
    code = fields.Char(
        string='Code'
    )
    description = fields.Text(
        string='Description'
    )
