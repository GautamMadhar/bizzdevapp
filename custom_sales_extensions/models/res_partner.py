# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, api,fields,_


class ResPartner(models.Model):
    _inherit = 'res.partner'

    display_name = fields.Char(compute='_compute_display_name', store=True)


    #2)In Many2one field of partner, it should include Ref in the format PARTNER NAME [REF].
    @api.depends('name', 'ref')
    def _compute_display_name(self):
        for partner in self:
            name = partner.name or ''
            if partner.ref:
                name = f"{name} [{partner.ref}]"
            partner.display_name = name
            
       
    # 1)Partner should be search on the Ref field from all Many2one widgets.
    @api.model
    def _name_search(self, name='', domain=None, operator='ilike', limit=None, order=None):
        domain = domain or []
        if name:
            name_domain = ['|', ('ref', operator, name), ('name', operator, name)]
            domain = ['&'] + name_domain + domain if domain else name_domain
        return self._search(domain, limit=limit, order=order)
