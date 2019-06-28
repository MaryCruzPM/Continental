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
	#count = fields.Integer(string='Repair Orders', compute='_datos_vehiculo')
	#x_v=fields.Many2one(related='id.fleet_repair_id.fleet_id')
	#@api.multi
	
	#@api.depends('id')
	#@api.onchange('id')
	#@api.multi
	# #@api.depends('id')
	# @api.multi
	# @api.depends('diagnose_id')
	# def _datos_vehiculo(self):
	# 	print("si escuch fleet repair")
	# 	#for order in self:
	# 	#	print("entrando a purchse")
	# 	#repair_order_ids = self.env['fleet_repair'].search([('sale_order_id'),'=',self.id])
	# 	#carro=repair_order_ids
	# 	#print(carro)
	# 	print("hola anteiror carro")
	# 	#self.x_vehiculo=repair_order_ids.fleet_id
	# 	print(self.x_vehiculo)


	
    # @api.onchange('id')
    # def _compute_product(self):
        
    #     id_x= self.env['fleet_repair'].search([('sale_order_id', '=', self.id)],limit=1)
    #     #print(id_x)
    #     #modelo=self.env['product.product'].search(['product_tmpl_id','=',id_x])
    #     print("metodo de product id")
    #     print("self")
        
    #     self.x_v=id_x.fleet_id
    #     print(self.x_v)
    #     print("anterior fleet id el vehiculo")
        
        #como se obtuve eb id_x el id de product.template entonces ya podemos accesar con ese id a su modelo y marca de product product porque 
        #estan los cmapos relacionales en product product para product template.

