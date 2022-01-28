# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LineaServicio( models.Model):
    _name = 'linea.servicio'
    _description = 'Modelo para la linea de los servicios'



    
    nombre_cargo = fields.Char( string = "Cargo")
    cantidad = fields.Integer( string = "Cantidad")
    precio_unidad = fields.Integer( string = "Precio")
    subtotal = fields.float( string = "Subtotal")

    