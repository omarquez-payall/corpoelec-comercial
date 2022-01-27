# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ContractAccounts( models.Model):
    _name = 'contract.accounts'
    _description = 'This model is to load Corpoelect customers contract accounts'
    
    #@api.model
    #def create(self, vals):
    #    vals['partner_code'] = self.env['ir.sequence'].next_by_code('partner_code_seq')
    #    result = super( ContractAccounts, self).create(vals)
    #    return result 

    #@api.model
    #def _get_next_sequence_number(self):
    #    for record in self:
    #        sequence = self.env['ir.sequence'].search([('code','=','partner_code_seq')])
    #        next= sequence.get_next_char(sequence.number_next_actual)
    #        return next