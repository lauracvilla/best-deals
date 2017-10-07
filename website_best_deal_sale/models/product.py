# -*- coding: utf-8 -*-
##############################################################################
#
#   Sell Discount Coupons
#   Authors: Dominador B. Ramos Jr. <mongramosjr@gmail.com>
#   Company: 3D2N World (http://www.3d2nworld.com)
#
#   Copyright 2016 Dominador B. Ramos Jr.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
##############################################################################


from odoo import models, fields, api, _

# defined for access rules
class Product(models.Model):
    _inherit = 'product.product'
    best_deal_coupon_ids = fields.One2many('best.deal.coupon', 'product_id', 'Deal Coupon')
    
