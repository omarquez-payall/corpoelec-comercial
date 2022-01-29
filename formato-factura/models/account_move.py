# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove( models.Model):
    _inherit = 'account.move'

    #------------------- Relacion con los servicios ------------------

    #------------ Servicio Electrividad ------------------------
    #electricidad_detalle = fields.One2many(
    #    comodel_name = "servicio.electricidad", 
    #    inverse_name = "factura_id")

    dias_lectura = fields.Integer( string = "Dias Lectura")
    # COMO DEBE ESTAR EN PRODUCCION
    #dias_lectura = fields.Integer( string = "Dias Lectura", required = True)

    #CREAR LINEAS DEL SERVICIO DE ELECTRICIDAD, ASEO Y RELLENO

    
    def cargar_productos_electricidad(self):
        for record in self:
            products = self.env['product.product'].search( [['precargar','=',True]])
            self.narration = products
            #for i in len( products):
            #    # CAMBIAR ACCOUNT_ID CUANDO SE SEPA A CUAL VA
            #    self.invoice_line.create({
            #        'name': products[i].name,
            #        'price_unit': products[i].price,
            #        'quantity': 1,
            #        'product_id': products[i].id,
            #        'account_id': 1
            #    })