# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions

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
    linea_electricidad = fields.One2many(
        comodel_name="linea.servicio", 
        inverse_name="move_id",
        
        states={'draft': [('readonly', False)]})
    
    """ cuenta_contrato = fields.One2many( 
        string="No Cuenta Contrato"
    ) """
    subtotal_electricidad = fields.Float( string="Subtotal Electricidad", store=True)
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

    @api.onchange('lectura_actual','lectura_anterior','factor_multiplicador','dias_lectura')
    def _compute_cantidad_medida( self):
        for record in self:
            record.cantidad_medida = ( record.lectura_actual - record.lectura_anterior) * record.factor_multiplicador
            if (record.dias_lectura > 0):
                record.kwh_equivalente = (record.cantidad_medida * 30) / record.dias_lectura
                linea_consumo = record.linea_electricidad.search([['clasificacion','=','consumo']])
                record.payment_reference = len( record.linea_electricidad)
                linea_consumo.update(
                    (1, linea_consumo.id, {
                        'cantidad': record.kwh_equivalente,
                        'precio_unidad':2
                    })
                )
            
    

    @api.onchange('linea_electricidad')
    def _onchange_subtotal(self):
        for record in self:
            if record.linea_electricidad is not None:
                record.subtotal_electricidad = 0
                for line in record.linea_electricidad:
                    record.subtotal_electricidad += line["subtotal"]


    

        