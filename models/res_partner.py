# -*- coding: utf-8 -*-

from odoo import models, api, fields, tools
import odoo.addons.decimal_precision as dp
from odoo.tools.translate import _
    
class ResPartner(models.Model):
    
    _inherit = "res.partner"

    meli_buyer_id = fields.Char('Meli Buyer Id')
    
    @api.model
    def process_fields_meli(self, values, doc_type):
        return values