# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Sales Extensions',
    'version': '1.0',
    'summary': 'Sales and Logistics customizations by Guatam Madhar',
    'description': 'Custom sales features for partner reference, tags, and more. Developed by Gautam.',
    'author': 'Gautam Madhar',
    'depends': ['sale', 'stock','sale_stock','web_studio','mrp','purchase'],
    'data': [
        'views/stock_picking_views.xml',
        'views/sale_order_views.xml',
        'data/automated_action.xml',
    ],
    'installable': True,
    'application': False,
}
