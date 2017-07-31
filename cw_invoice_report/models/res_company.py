# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################

from openerp import models, fields, api, _
from openerp.exceptions import except_orm


class res_company(models.Model):
    _inherit = 'res.company'
    
    sec_image = fields.Binary("Sec Image", attachment=True)
    
