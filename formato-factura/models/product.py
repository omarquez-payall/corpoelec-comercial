# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Product( models.Model):
    _inherit = 'product.product'

    #------------------- Campo para identificar productos precargados en factura electricidad ------------------

    
    precargar = fields.Boolean( string = "Precargar", default = False)
    