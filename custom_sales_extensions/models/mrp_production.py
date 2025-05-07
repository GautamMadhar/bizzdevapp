# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'


    #Manufacturing orders created from sale order should not allowed to change the qty after the confirmation.
    @api.onchange('qty_producing')
    def _onchange_qty_block_post_confirm(self):
        if self.state not in ('draft'):
            sale_order_ids = self.procurement_group_id.mrp_production_ids.move_dest_ids.group_id.sale_id.ids
            if sale_order_ids:
                raise UserError("This MO is linked with Sale order so you cannot change quantity after confirmation.")
