# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Electricidad( models.Model):
    _inherit = 'account.move'
    #_name = "servicio.electricidad"
    #_description = "Modelo creado para el detalle del servicio de electricidad"

    #-------------- FACTURA ---------------------------------------
    #lineas_detalle = fields.
    #factura_id = fields.Many2one(
    #    comodel_name = "account.move"
    #)
    #dias_lectura = fields.Integer( string ="Dias Lectura", related ="factura_id.dias_lectura")

    #-------------- SECCION DE CONSUMO ----------------------------
    lectura_actual = fields.Integer( string = "Lectura Actual", store=True)
    lectura_anterior = fields.Integer( string = "Lectura Anterior", store=True)
    factor_multiplicador = fields.Integer( string = "Factor Multiplicador", store=True)
    cantidad_medida = fields.Integer( string = "Cantidad Medida")
    kwh_equivalente = fields.Float( string = "kwh Equivalente")
    monto_total_consumo = fields.Integer( string = "Monto total consumo", store=True)

    #-------------- SECCION DE DEMANDA ---------------------------
    demanda_asignada = fields.Integer( string = "Demanda asignada", store=True)
    demanda_leida = fields.Integer( string = "Demanda Leida", store=True)
    demanda_facturada = fields.Integer( string = "Demanda Facturada", store=True)
    monto_total_demanda = fields.Integer( string = "Monto total demanda", store=True)

    @api.onchange('lectura_actual','lectura_anterior','factor_multiplicador')
    def _compute_cantidad_medida( self):
        for record in self:
            record.cantidad_medida = ( record.lectura_actual - record.lectura_anterior) * record.factor_multiplicador
            record.kwh_equivalente = (record.cantidad_medida * 30) / record.dias_lectura