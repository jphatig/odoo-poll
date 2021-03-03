# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from dateutil.relativedelta import relativedelta
from datetime import datetime

class Partner(models.Model):
    """Defines citizen data"""

    _inherit = 'res.partner'

    is_person = fields.Boolean(
        string='Is a person'
    )
    photo = fields.Binary(
        string='Photo'
    )
    document_type = fields.Selection(
        string='ID Type',
        selection=[
            ('personal', 'Personal ID'),
            ('passport', 'Passport'),
            ('other', 'Another ID type')
        ]
    )
    document = fields.Char(
        string='ID number'
    )
    birth_date = fields.Date(
        string='Birth Date'
    )
    age = fields.Integer(
        string='Age (years)',
        compute='_compute_age'
    )
    gender_id = fields.Many2one(
        comodel_name='res.partner.gender',
        string='Gender'
    )
    preferred_gender_id = fields.Many2one(
        comodel_name='res.partner.gender',
        string='Preferred gender for poll'
    )
    residence_geounit_id = fields.Many2one(
        comodel_name='poll.geounit',
        string='Residence Location'
    )
    residence_hierarchy = fields.Char(
        string='Complete Residence Location',
        related='residence_geounit_id.hierarchy'
    )

    @api.onchange('gender')
    def onchange_gender(self):
        if not (self.id and self.preferred_gender):
            self.preferred_gender = self.gender

    def _compute_age(self):
        for record in self:
            record.age = relativedelta(datetime.now(), self.birth_date).years
