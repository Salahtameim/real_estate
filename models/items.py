
from odoo import models, fields

class Items(models.Model):

    _name = "items"
    _description = "Item Name"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    code = fields.Char(
        string="Item Code",
        copy=True,
        required=True
    )

    name = fields.Char(
        string="Item Name",
        copy=True,
        required=True
    )
