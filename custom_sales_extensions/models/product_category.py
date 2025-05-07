# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models,api
from odoo.exceptions import ValidationError


class ProductCategory(models.Model):
    _inherit = 'product.category'


    # Category should have unique name.
    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Category name must be unique.')
    ]
    
    
    # Category should have unique name.
    @api.constrains('name')
    def _check_unique_name(self):
        for record in self:
            if self.search_count([
                ('name', '=', record.name),
                ('id', '!=', record.id)
            ]):
                raise ValidationError("Category name must be unique.")
