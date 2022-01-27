# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove( models.Model):
    _inherit = 'account.move'

    #------------------- Relacion con los servicios ------------------

    #------------ Servicio Electrividad ------------------------
    electricidad_detalle = fields.One2many(
        comodel_name = "servicio.electricidad", 
        inverse_name = "factura_id")

    dias_lectura = fields.Integer( string = "Dias Lectura", required = True)


    #------------ Servicio Aseo --------------------------------

    #------------ Servicio Relleno Sanitario -------------------