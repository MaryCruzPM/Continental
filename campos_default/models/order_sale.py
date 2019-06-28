# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

# from odoo import fields, models, api,
# from datetime import date, time, datetime
# from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

# class SaleOrder(models.Model):
#     _inherit = 'sale.order'
    
    
#     x_vehiculo = fields.Many2one('fleet.vehicle', string="Vehiculo")
#     x_marca=fields.Many2one('fleet.vehicle.model.brand')
#     x_modelo=fields.Many2one('fleet.vehicle.model')
#     x_Matricula=fields.Char()
#     x_year_modelo=fields.Char()
#     x_unidad=fields.Char()

 #    @api.multi
 #    @api.depends('id')
 #    def _datos_vehiculo(self):
 #       print("holaaaaaa")
 #       #value=8
 #       #busqueda=self.env['fleet.repair'].search(['sale_order_id','=',self.id])
 #       #self.x_vehiculo=busqueda.fleet_id
 #        #for order in self:
 #        #	print("hola")
 #       		# repair=self.env['fleet.repair'].search(([('sale_order_id', '=', order.id)])
 #       		# if repair:
	#        	# 	self.x_vehiculo=repair.fleet_id
	#        	# 	print(self.x_vehiculo)


	# @api.multi
 #    @api.depends('fleet_repair_id')
 #    def _compute_repair_id(self):
 #        for order in self:
 #            repair_order_ids = self.env['fleet.repair'].search([('sale_order_id', '=', order.id)])            
 #            order.count_fleet_repair = len(repair_order_ids)



 #    count=fields.Integer(string='repeir', compute='_hola')




# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api
# modelo de campos a editar desde factura borrados
class editable(models.Model):
	_inherit='sale.order'


	x_vehiculo = fields.Many2one('fleet.vehicle', string="Vehiculo")
	x_marca = fields.Many2one('fleet.vehicle.model.brand')
	x_modelo = fields.Many2one('fleet.vehicle.model')
	x_Matricula = fields.Char()
	x_year_modelo = fields.Char()
	x_unidad =fields.Char()
	#count = fields.Integer(string='Repair Orders', compute='_compute_repair_ok')
	#vari = fields.Integer(string='Work Orders', compute='_valor')
	# vari=fields.Integer(string='hola', compute='_valor')
 #    @api.multi
 #    @api.depends('x_marca')
 #    def _valor(self):
 #    	print("hola")
    
	# @api.multi 
	# @api.depends('state')
	# def _valor(self):
	# 	print("hola")
	# 	for order in self:
 #            repair_t = self.env['fleet.repair'].search([('sale_order_id', '=', order.id)])            
 #            order.count_fleet_repair = len(repair_order_ids)

		#self.x_vehiculo=repair_t.fleet_id
		#print(self.x_vehiculo)

	# @api.multi
	# @api.depends('x_unidad')
	# 	def _valor(self):
	# 		print("hla")

	@api.multi
	@api.depends('state')
	def _compute_repair_id_x(self):
		print("dentor de unidad")
		# for order in self:
		# 	repair_order_ids = self.env['fleet.repair'].search([('sale_order_id','=',order.id)])
		# 	print("holaaaaaaa***")
		# 	order.x_vehiculo=repair_order_ids.fleet_id
		print(self.id)
		print(self)
		print(self.name)
		print(self.x_vehiculo)
		repair_x=self.env['fleet.repair'].search([('sale_order_id','=',self.id)])
		self.x_vehiculo=repair_x.fleet_id
		print(self.x_vehiculo.name)
		print(repair_x.fleet_id.model_id)
		print(repair_x.fleet_id.license_plate)
		print(repair_x.fleet_id.name)
		print(repair_x)
		print(repair_x.name)
		print(repair_x.fleet_repair_line.fleet_id.model_id.name)
		print(repair_x.fleet_repair_line.fleet_id.license_plate)
		print(repair_x.fleet_repair_line.fleet_id.brand_id.name)
		print(repair_x.fleet_id.model_year) #se accede a fleet repair a vehiculo, de ahi al año del vehiculo
		self.x_modelo=repair_x.fleet_repair_line.fleet_id.model_id.name
		self.x_Matricula=repair_x.fleet_repair_line.fleet_id.license_plate
		self.x_marca= repair_x.fleet_repair_line.fleet_id.brand_id.name
		#self.x_vehiculo= self.x_modelo+'/'+self.x_marca+'/'+self.x_Matricula
		self.x_modelo.write({'name':[(1, repair_x.fleet_repair_line.fleet_id.model_id,{repair_x.fleet_repair_line.fleet_id.model_id.name})]})


	count = fields.Integer(compute='_compute_repair_id_x',string="hola")