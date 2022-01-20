# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceImagesInherit( models.Model):
    _inherit = 'account.move'
    images = fields.Many2one( string = 'Imágenes para facturas', comodel_name = 'invoices.images')
    
    @api.model
    def get_data_from_invoice_images(self):
        for record in self:
            record.images = self.env['invoices.images'].search([('id','=', 1)])