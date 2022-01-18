# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceImages( models.Model):
    _inherit = 'account.move'
    logo = fields.Binary(string='Logo')
    header_logo = fields.Binary(string='Header Logo')
    full_logo = fields.Binary(string='Full Logo')
    payment_methods = fields.Binary(string='Payment Methods')
    
    @api.model
    def create(self, vals):
        vals['logo','header_logo','full_logo','payment_methods'] = self.env['invoices.images'].export_data('logo','header_logo','full_logo','payment_methods')
        result = super(InvoiceImages, self).create(vals)
        return result 