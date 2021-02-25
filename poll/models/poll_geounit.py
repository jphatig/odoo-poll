# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

class GeoUnit(models.Model):
    """Defines a group of land limited by border lines"""

    _name = 'poll.geounit'

    name = fields.Char(
        string='Name',
        required=True
    )
    code = fields.Char(
        string='Code'
    )
    complete_code = fields.Char(
        string='Complete code',
        compute='_complete_code'
    )
    hierarchy = fields.Char(
        string='Hierarchy',
        compute='_hierarchy'
    )
    parent_id = fields.Many2one(
        string='Parent',
        comodel_name='poll.geounit'
    )
    type_id = fields.Many2one(
        string='Type',
        comodel_name='poll.geounit.type',
        required=True
    )
    parent_type_id = fields.Many2one(
        string='Parent type',
        comodel_name='poll.geounit.type',
        related='type_id.parent_id',
        readonly=True
    )
    child_type_id = fields.Many2one(
        string='Child type',
        comodel_name='poll.geounit.type',
        related='type_id.child_id'
    )
    child_ids = fields.One2many(
        string='Childs',
        comodel_name='poll.geounit',
        inverse_name='parent_id'
    )

    _sql_constraints = [
        ('code_type_unique',
         'UNIQUE(code, type_id)',
         'Code can not be repeated per type'),
    ]

    def _complete_code(self):
        """Set complete code using parent's code"""
        for record in self:
            record.complete_code = ''.join(record._get_parent_codes())

    def _get_parent_codes(self, codes=[]):
        """Get parent's code recursively"""
        codes = [self.code or ''] + codes
        if self.parent_id.code:
            return self.parent_id._get_parent_codes(codes=codes)
        return codes

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
