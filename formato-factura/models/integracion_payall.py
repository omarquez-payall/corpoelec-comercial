# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions


class IntegacionPayall( models.Model):
    _name ='integracion.payall'
    _description = 'Modelo para la integracion con Payall a traves de la API'

    @api.model 
    def consultaDeudaCliente(self, res_partner_code):
        if (res_partner_code is None):
            result = { 
                "code":"C7",
                "message":"El codigo del cliente no fue recibido correctamente por el servidor"
            }
            return result
        partner = self.env['res.partner'].search([['partner_code','=',res_partner_code]])
        if ( partner is None):
            result = { 
                "code":"X4",
                "message":"El cliente no existe"
            }
            return result
        invoices = self.env['account.move'].search([
            ['partner_id.id','=', partner.id], 
            ['move_type','=','out_invoice'],
            ['payment_state','=','not_paid'],
            ['payment_state','=','not_paid']
        ])
        if ( invoices is None):
            result = { 
                "code":"V4",
                "message":"El cliente no posee deuda a cancelar"
            }
            return result
        amount_due = 0
        for invoice in invoices:
            amount_due += invoice.amount_residual
        result = {
            "code":"00",
            "amount": amount_due
        }
        return result
    
    @api.model
    def pagarDeudaCliente(self, amount, res_partner_code):
        if (amount is None):
            result = { 
                "code":"M4",
                "message":"El monto no fue recibido correctamente por el servidor"
            }
            return result
        if ( res_partner_code is None):
            result = { 
                "code":"I7",
                "message":"Identificador del cliente no fue recibido correctamente por el servidor"
            }
            return result
        invoices = self.env['account.move'].search([['partner_id.id','=', res_partner_code], ['move_type','=','out_invoice'], ['payment_state','=','not_paid']])
        if ( invoices is None):
            result = { 
                "code":"V4",
                "message":"El cliente no posee deuda a cancelar"
            }
            return result
        payment_method = self.env['account.payment.method'].search([['code','=','manual'],['payment_type','=','inbound']])
        active_ids = invoices.ids
        payments = self.env['account.payment.register'].with_context(active_model='account.move', active_ids=active_ids).create({
            'amount': amount,
            'group_payment': True,
            'payment_difference_handling': 'open',
            'currency_id': self.env.company['currency_id'].id,
            'payment_method_id': payment_method.id,
        })._create_payments()
        return payments.payment_difference
 
