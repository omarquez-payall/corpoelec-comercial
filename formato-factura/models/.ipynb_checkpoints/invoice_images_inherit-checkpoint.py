# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InvoiceImagesInherit( models.Model):
    _inherit = 'account.move'
    images = fields.Many2one( string = 'Imágenes para facturas', comodel_name = 'invoices.images', required = True)
    logo = fields.Binary(string='Logo', related='images.logo')
    header_logo = fields.Binary(string='Header Logo', related='images.header_logo')
    full_logo = fields.Binary(string='Full Logo', related='images.full_logo')
    payment_methods = fields.Binary(string='Payment Methods', related='images.payment_methods')