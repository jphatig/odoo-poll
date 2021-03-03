# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class Candidate(models.Model):
    """Defines partner as candidates"""

    _name = 'poll.candidate'

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Person',
        domain=[('is_person', '=', True)]
    )
    name = fields.Char(
        string='Name',
        related='partner_id.name'
    )
    document_type = fields.Selection(
        string='ID Type',
        related='partner_id.document_type',
        selection=[
            ('personal', 'Personal ID'),
            ('passport', 'Passport'),
            ('other', 'Another ID type')
        ]
    )
    document = fields.Char(
        string='ID number',
        related='partner_id.document',
    )
    photo = fields.Binary(
        string='Photo',
        related='partner_id.photo'
    )
    charge_id = fields.Many2one(
        comodel_name='poll.charge',
        string='Charge for apply'
    )
    charge_geounit_type_id = fields.Many2one(
        comodel_name='poll.geounit.type',
        string='Geolocation charge type',
        related='charge_id.geounit_type_id'
    )
    event_id = fields.Many2one(
        comodel_name='poll.event',
        string='Event'
    )
    political_party_id = fields.Many2one(
        comodel_name='poll.political.party',
        string='Political Party'
    )
    political_party_logo = fields.Binary(
        string='Photo',
        related='political_party_id.logo'
    )
    geounit_id = fields.Many2one(
        comodel_name='poll.geounit',
        string='Geolocation jurisdiction'
    )
