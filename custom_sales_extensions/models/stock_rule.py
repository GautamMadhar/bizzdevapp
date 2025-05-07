# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api,fields,_

class StockRule(models.Model):
    _inherit = 'stock.rule'

    def _make_po_get_domain(self, procurements):
        """
        Group procurements by company, rule, warehouse, vendor, and category.
        """
        domain = super()._make_po_get_domain(procurements)
        # Extend domain with product category id (ensure same category in group)
        if procurements:
            category_id = procurements[0].product_id.categ_id.id or False
            domain += [('categ_id', '=', category_id)]
        return domain
    
    
    def _prepare_purchase_order(self, company, partner, warehouse, category=None, origin=None, values=None):
        po_vals = super()._prepare_purchase_order(company, partner, warehouse, category, origin, values)
        if category:
            po_vals['categ_id'] = category.id
        return po_vals