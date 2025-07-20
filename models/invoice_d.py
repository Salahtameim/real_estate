from odoo import models, fields
class Inv_d(models.Model):

    _name = "invoice_d"
    _description = "Cash Sale Item"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    item_code = fields.Char(
        string="Item Code",
        copy=True,
        required=True,
        related="item_id.code"
    )
    item_id = fields.Many2one(
        comodel_name="items",
        ondelete="restrict",
        string="Item Name",
        copy=True,
        required=True

   )
    qty = fields.Float(
        string="Qty",
        copy=True,
        required=True
    )
    price = fields.Float(
        string="Price",
        copy=True,
        required=True
    )
    gross = fields.Float(
        string="G.Total",
        copy=True,
        required=True
    )
    disc = fields.Float(
        string="Disc",
        copy=True,
        required=True
    )
    vat = fields.Float(
        string="Vat 15%",
        copy=True,
        required=True
    )
    total = fields.Float(
        string="Total amount",
        copy=True,
        required=True
    )
    invoice_id = fields.Many2one(
        comodel_name="invoice_h",
        ondelete="restrict",
        string="Related real estate",
        copy=True,
        required=True
    )