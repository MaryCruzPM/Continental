# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api
# modelo de campos a editar desde factura borrados
class vista_lista(models.Model):
	_inherit='fleet.repair'

	#x_matricula=fields.Char(compute='_compute_vista')
	license_plate = fields.Char('License Plate', compute='_compute_vista', help='License plate number of the vehicle (ie: plate number for a car)',
		search   ='_search_stage_fold',
	        inverse  ='_write_stage_fold')


	def _search_stage_fold(self,operator,value): #fumción para hacer que pueda haber una busqueda aunque el campos sea computado
		return[('fleet_repair_line.license_plate',operator,value)]

	def _write_stage_fold(self):
	 	self.license_plate=self.fleet_repair_line.license_plate
	
	stage_fold = fields.Boolean(
	        string   = 'Stage Folded?',
	        compute  ='_compute_stage_fold',
	                  # store=False) # predeterminado
	        search   ='_search_stage_fold',
	        inverse  ='_write_stage_fold')
   	
	@api.one
	@api.depends('fleet_repair_line')
	def _compute_vista(self):
		for order in self:
			print(order.fleet_repair_line.license_plate)
			order.license_plate=order.fleet_repair_line.license_plate


 #    # def _search_stage_fold(self, operator, value):
 #    # return [('stage_id.fold', operator, value)]

	# def _write_stage_fold(self):
	#     self.stage_id.fold = self.stage_fold