# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class ResPartnerTechnician(models.Model):
    _inherit = 'fleet.diagnose'
    
    user_id = fields.Many2one('res.partner', string='Mecánico')

class ResPartnerDiagnise(models.TransientModel):
    _inherit = 'fleet.diagnose.assignto.technician'
    
    user_id = fields.Many2one('res.partner', string='Mecánico')

