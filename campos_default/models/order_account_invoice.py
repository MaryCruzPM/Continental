# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api
# modelo de campos a editar desde factura borrados
class factura(models.Model):
	_inherit='account.invoice'

	x_vehiculo = fields.Many2one('fleet.vehicle',string="Vehiculo")
	x_marca = fields.Many2one('fleet.vehicle.model.brand')
	x_modelo = fields.Many2one('fleet.vehicle.model')
	x_Matricula = fields.Char()
	x_year_modelo = fields.Char()
	x_unidad =fields.Char()
	x_kilometraje=fields.Float()
	x_unidadKilometro=fields.Selection(selection=[('kilometers','Kilómetros'),('Miles','Millas')],)

# 	@api.model_create_multi
# 	def create(self,vals):
# 		print("dentro de unidad")
# 		#if vals.get('origin'):
# 		sale_obj = self.env['sale.order'].search([('name', '=', vals.get('origin'))])
# 		print(sale_obj.fleet_repair_id.fleet_id.id)
# 		print(sale_obj)
# 		print(sale_obj.name)
# 		res = super(factura, self).create(vals)
# 		print(res)
# 		print(res.id)
# 		repair_x=self.env['fleet.repair'].search([('id','=',sale_obj.fleet_repair_id.id)],limit=1)
# 		print(repair_x)
# 		print(repair_x.fleet_repair_line.fleet_id.model_id)
# 		#res.write({'x_modelo':[(4,repair_x.fleet_repair_line.fleet_id.model_id)]})
# 		res.x_modelo=repair_x.fleet_repair_line.fleet_id.model_id
# 		res.x_marca=repair_x.fleet_repair_line.fleet_id.brand_id
# 		res.x_Matricula=repair_x.fleet_repair_line.fleet_id.license_plate
# 		res.x_year_modelo=repair_x.fleet_repair_line.fleet_id.model_year
# 		res.x_unidad=repair_x.fleet_repair_line.fleet_id.x_numero_unidad
# 		res.x_kilometraje=repair_x.fleet_repair_line.fleet_id.odometer
# #		res.x_unidadKilometro=repair_x.fleet_repair_line.fleet_id.odometer_unit
# 		res.x_vehiculo=repair_x.fleet_repair_line.fleet_id
# 		return res

	@api.model_create_multi
	def create(self,vals):
		print("dentro de unidad")
		res = super(factura, self).create(vals)
		print(res)
		print(res.id)
		print(res.origin)
		if res.origin:

			sale_order=self.env['sale.order'].search([('name','=',res.origin)],limit=1)
			repair_x=self.env['fleet.repair'].search([('id','=',sale_order.fleet_repair_id.id)],limit=1)
			print(repair_x)
			print(repair_x.fleet_repair_line.fleet_id.model_id)
			#res.write({'x_modelo':[(4,repair_x.fleet_repair_line.fleet_id.model_id)]})
			res.x_modelo=repair_x.fleet_repair_line.fleet_id.model_id
			res.x_marca=repair_x.fleet_repair_line.fleet_id.brand_id
			res.x_Matricula=repair_x.fleet_repair_line.fleet_id.license_plate
			res.x_year_modelo=repair_x.fleet_repair_line.fleet_id.model_year
			res.x_kilometraje=repair_x.fleet_repair_line.fleet_id.odometer
			res.x_unidadKilometro=repair_x.fleet_repair_line.fleet_id.odometer_unit
			res.x_vehiculo=repair_x.fleet_repair_line.fleet_id

		return res


#/odoo/odoo-server/addons/sale/models
	
	