# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class StockPickingType(models.Model):
    _inherit = "stock.picking.type"

    set_carrier_connection = fields.Boolean(
        string="Set Carrier Connection"
    )
