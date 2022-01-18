# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceImages( models.Model):
    _name = 'invoices.images'
    _description = 'This model is to load and manage the images needed for the invoice template'
    logo = fields.Binary(string='Logo')
    header_logo = fields.Binary(string='Header Logo')
    full_logo = fields.Binary(string='Full Logo')
    payment_methods = fields.Binary(string='Payment Methods')
    
    @api.model
    def export_data(self):
        return [self.logo,self.header_logo,self.full_logo,self.payment_methods]