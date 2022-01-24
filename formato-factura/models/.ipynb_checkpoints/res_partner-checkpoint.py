# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PartnerCodeInherit( models.Model):
    _inherit = 'res.partner'
    partner_code = fields.Many2one(string = 'Código de Interlocutor', default=lambda self: self._get_next_sequence_number())
    
    @api.model
    def create(self, vals):
        vals['partner_code'] = self.env['ir.sequence'].next_by_code('partner_code_seq')
        result = super( PartnerCodeInherit, self).create(vals)
        return result 

    @api.model
    def _get_next_sequence_number(self):
        sequence = self.env['ir.sequence'].search([('code','=','partner_code_seq')])
        next= sequence.get_next_char(sequence.number_next_actual)
        return next