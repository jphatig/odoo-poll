# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class PartnerGender(models.Model):
    """Defines partner gender"""

    _name = 'res.partner.gender'

    name = fields.Char(
        string='Name',
        required=True
    )
