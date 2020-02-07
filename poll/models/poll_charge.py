# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Charge(models.Model):
    """Defines charges which ones a canditate could be elected"""

    _name = 'poll.candidate'

    name = fields.Char(
        string='Name'
    )
    active = fields.Boolean(
        string='Active'
    )
