# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove( models.Model):
    _inherit = 'account.move'

    #------------------- Relacion con los servicios ------------------
    No_Contable = fields.Char( string = 'No Doc Contable', required = True, index=True, default=lambda self: self._get_next_sequence_number("Seq_No_Contable"))
    No_Registro = fields.Char( string = 'No Registro', required = True, index=True, default=lambda self: self._get_next_sequence_number("Seq_No_Registro"))
    
    inicio_periodo = fields.Date(string='Inicio período', default=fields.Date.today, store=True)
    fin_periodo = fields.Date(string='Fin período', default=fields.Date.today, store=True)
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

    @api.model
    def create(self, vals):
        vals['No_Contable'] = self.env['ir.sequence'].next_by_code('Seq_No_Contable')
        vals['No_Registro'] = self.env['ir.sequence'].next_by_code('Seq_No_Registro')
        result = super(AccountMove, self).create(vals)
        return result 

    @api.model
    def _get_next_sequence_number(self, seq_code):
        sequence = self.env['ir.sequence'].search([('code','=', seq_code)])
        next= sequence.get_next_char(sequence.number_next_actual)
        return next

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
            record.linea_electricidad.create({
                'move_id': record.id,
                'nombre_cargo': 'FACTURACION POR CONSUMO',
                'cantidad': 1,
                'tipo':'principal',
                'clasificacion':'consumo',
                'precio_unidad':1,
                'subtotal':1
            })
            record.linea_electricidad.create({
                'move_id': record.id,
                'nombre_cargo': 'CARGO POR AJUSTE COMBUSTIBLE Y ENERGIA',
                'cantidad': 1,
                'tipo':'otro',
                'clasificacion':'combustible',
                'precio_unidad':1,
                'subtotal':1
            })
            record.linea_electricidad.create({
                'move_id': record.id,
                'nombre_cargo': 'FACTURACION POR DEMANDA',
                'cantidad': 1,
                'tipo':'principal',
                'clasificacion':'demanda',
                'precio_unidad':1,
                'subtotal':1
            })