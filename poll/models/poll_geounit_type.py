# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class GeoUnitType(models.Model):
    """Defines types for geounits"""

    _name = 'poll.geounit.type'

    name = fields.Char(
        string='Name',
        required=True
    )
    hierarchy = fields.Char(
        string='Hierarchy',
        compute='_hierarchy'
    )
    parent_id = fields.Many2one(
        string='Parent',
        comodel_name='poll.geounit.type'
    )
    child_id = fields.Many2one(
        string='Child',
        comodel_name='poll.geounit.type',
        compute='_child_id'
    )
    event_id = fields.Many2one(
        string='Event',
        comodel_name='poll.event'
    )

    _sql_constraints = [
        ('parent_unique',
         'UNIQUE(parent_id)',
         'Type should have an unique parent'),
    ]

    @api.multi
    def _child_id(self):
        """Sets type's child"""
        for record in self:
            record.child_id = self.search([('parent_id', '=', record.id)])

    @api.constrains('parent_id')
    def manage_child(self):
        """Sets parent's child based on self"""
        self.parent_id.child_id = self.id

    @api.multi
    def _hierarchy(self):
        """Defines hierarchy string description"""
        for record in self:
            record.hierarchy = '/'.join(record._get_parent_names())

    def _get_parent_names(self, names=[]):
        """Search parents and join them recursively"""
        names = [self.name or ''] + names
        if self.parent_id.name:
            return self.parent_id._get_parent_names(names=names)
        return names
