# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api,fields,_


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    categ_id = fields.Many2one('product.category', string='Product Category')