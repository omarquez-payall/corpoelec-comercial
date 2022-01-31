# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LineaServicio( models.Model):
    _name = 'linea.servicio'
    _description = 'Modelo para la linea de los servicios'



    move_id = fields.Many2one( comodel_name = "account.move", string = "Linea de Servicio")
    nombre_cargo = fields.Char( string = "Cargo")
    cantidad = fields.Integer( string = "Cantidad")
    precio_unidad = fields.Float( string = "Precio")
    subtotal = fields.Float( string = "Subtotal")

    