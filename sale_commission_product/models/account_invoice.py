# -*- coding: utf-8 -*-
# © 2015 Alejandro Sánchez Ramírez (<http://www.asr-oss.com>)
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, models
import logging
_logger = logging.getLogger(__name__)


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    # CORREGIR ERROR
    @api.constrains('product_id')
    def commission_product_id(self):
        for rec in self:
            if rec.move_id.move_type in ('out_invoice', 'out_refund') and rec.partner_id and rec.product_id:
                agent = self.move_id.user_id.partner_id
                commission_id = agent.commission_id.id
                commission_id_product = self.env["product.product.agent"]\
                    .get_commission_id_product(self.product_id.id, agent)
                if commission_id_product:
                    commission_id = commission_id_product
                agent_list = []
                for rec in self:
                    agent_list.append({'agent_id': agent.id,
                                       'object_id': rec._origin.id,
                                       'commission_id': commission_id,
                                       })
                self.agent_ids = [(0, 0, x) for x in agent_list]
                _logger.info('***paso la creacion**')
