# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove( models.Model):
    _inherit = 'account.move'

    #------------------- Relacion con los servicios ------------------
    linea_electricidad = fields.One2many(
        comodel_name="linea.servicio", 
        inverse_name="move_id",
        
        states={'draft': [('readonly', False)]})
    #------------ Servicio Electrividad ------------------------
    #electricidad_detalle = fields.One2many(
    #    comodel_name = "servicio.electricidad", 
    #    inverse_name = "factura_id")

    dias_lectura = fields.Integer( string = "Dias Lectura")
    cargar_productos = fields.Boolean( string="Cargar", default = False)
    saldo_vencido = fields.Float( string="Saldo Vencido", default = 0.0)
    # COMO DEBE ESTAR EN PRODUCCION
    #dias_lectura = fields.Integer( string = "Dias Lectura", required = True)
    #CREAR LINEAS DEL SERVICIO DE ELECTRICIDAD, ASEO Y RELLENO

    
    def cargar_productos_electricidad(self):
        for record in self:
            products = self.env['product.product'].search( [['precargar','=',True]])
            
            for product in products:
                #CAMBIAR ACCOUNT_ID CUANDO SE SEPA A CUAL VA
                record.invoice_line_ids.create({
                    'name': product.name,
                    'price_unit': product.price,
                    'quantity': 1,
                    'product_id': product.id,
                    'account_id': 1,
                    'move_id': record.id
                })
                record.cargar_productos = True