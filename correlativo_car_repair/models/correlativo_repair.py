# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api, _
from datetime import date, time, datetime
from odoo import tools
from odoo.exceptions import UserError, ValidationError


class correlativo_repair(models.Model):
    _inherit = 'fleet.repair'
    #valor= fields.Char(compute='default_get')
    #count_fleet_repair  = fields.Integer(string='Repair Orders', compute='_compute_repair_id')
    
    @api.model # en esta funcion modifico que no saque la secuencia por defaul 
    def default_get(self,fields):
        res = super(correlativo_repair, self).default_get(fields)
        res['sequence'] = "Nuevo"
        res['receipt_date'] = datetime.now()
        #if self.fleet_id:
        #	res['sequence'] = self.env['ir.sequence'].get('fleet.repair')
        #	res['receipt_date'] = datetime.now()
        #print(res)
        return res


    @api.multi
    def create(self,vals):
    	reparacion=super(correlativo_repair,self).create(vals)
    	secuencia=self.env['ir.sequence'].get('fleet.repair')
    	reparacion.write({'sequence':secuencia})
    	return reparacion


