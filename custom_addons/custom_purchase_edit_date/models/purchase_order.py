from odoo import models, fields # type: ignore


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    date_approve = fields.Datetime(
        string="Fecha de confirmación",
        readonly=False
    )
