# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api
# modelo de campos a editar desde factura borrados
class vista_lista_diagnostico(models.Model):
	_inherit='fleet.diagnose'

	#x_matricula=fields.Char(compute='_compute_vista_diagnostico')
	license_plate = fields.Char('License Plate', compute='_compute_vista_diagnostico', help='License plate number of the vehicle (ie: plate number for a car)')
	@api.multi
	@api.depends('fleet_repair_line')
	def _compute_vista_diagnostico(self):
		for order in self:
			print(order.fleet_repair_line.license_plate)
			order.license_plate=order.fleet_repair_line.license_plate

class vista_lista_order_trabajo(models.Model):
	_inherit='fleet.workorder'

	#x_matricula=fields.Char(compute='_compute_vista_order_trabajo')
	license_plate = fields.Char('License Plate', compute='_compute_vista_order_trabajo',help='License plate number of the vehicle (ie: plate number for a car)')
    
	@api.multi
	@api.depends('fleet_repair_line')
	def _compute_vista_order_trabajo(self):
		for order in self:
			print(order.fleet_repair_line.license_plate)
			order.license_plate=order.fleet_repair_line.license_plate