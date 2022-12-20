# -*- coding: utf-8 -*-
# © 2015 Alejandro Sánchez Ramírez (<http://www.asr-oss.com>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.constrains('product_id')
    def constrains_product_id(self):
        #res = super(SaleOrderLine, self)._onchange_product_id()
        res = self
        _logger.info("***_onchange_product_id****")
        partner = self.env["res.partner"].browse(
            self.order_id.partner_id.id)
        if partner and self.product_id:
            # for agent in partner.agent_ids:
            # default commission_id for agent
            agent = self.order_id.user_id.partner_id
            commission_id = agent.commission_id.id
            commission_id_product = self.env["product.product.agent"]\
                .get_commission_id_product(self.product_id.id, agent)
            if commission_id_product:
                commission_id = commission_id_product
            agent_list = []
            agent_list.append({'agent_id': agent.id,
                               'object_id': self._origin.id,
                               'commission_id': commission_id,
                               })
            self.agent_ids = [(0, 0, x) for x in agent_list]
            _logger.info('***paso la creacion**')
