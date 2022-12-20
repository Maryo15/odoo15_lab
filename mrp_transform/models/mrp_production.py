# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

import logging

_logger = logging.getLogger(__name__)


class MrpProduction(models.Model):
    """ Manufacturing Orders """
    _inherit = 'mrp.production'

    def consume_moves(self):
        for rec in self:
            _logger.info(
                "{}*************".format(rec.name)
            )
            for mri in rec.move_raw_ids:
                if mri.state not in ('partially_available', 'assigned'):
                    continue
                for move_line in mri.move_line_ids:
                    if mri.has_tracking != 'none' and not (move_line.lot_id or move_line.lot_name):
                        continue
                    move_line.qty_done = move_line.product_uom_qty

        lines = self.env['stock.move.line'].search([('reference', '=', rec.name)])
        for x in lines:
            x.state = 'done'
